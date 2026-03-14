from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import CareerPath, EducationResource, UserProfile
from .forms import UserProfileForm


def get_or_create_profile(user):
    profile, _ = UserProfile.objects.get_or_create(user=user)
    return profile


class CareerHomeView(View):
    template_name = 'career_edu/home.html'

    def get(self, request):
        career_paths = CareerPath.objects.all()[:6]
        resources = EducationResource.objects.all()[:6]
        context = {
            'career_paths': career_paths,
            'resources': resources,
            'total_careers': CareerPath.objects.count(),
            'total_resources': EducationResource.objects.count(),
        }
        return render(request, self.template_name, context)


class DashboardView(LoginRequiredMixin, View):
    template_name = 'career_edu/dashboard.html'
    login_url = 'login'

    def get(self, request):
        profile = get_or_create_profile(request.user)
        recommended_careers = profile.get_recommended_careers()
        recommended_resources = profile.get_recommended_resources()
        context = {
            'profile': profile,
            'recommended_careers': recommended_careers,
            'recommended_resources': recommended_resources,
            'total_careers': CareerPath.objects.count(),
            'total_resources': EducationResource.objects.count(),
        }
        return render(request, self.template_name, context)


class CareerExploreView(View):
    template_name = 'career_edu/career_explore.html'

    def get(self, request):
        domain_filter = request.GET.get('domain', '')
        search_query = request.GET.get('q', '')
        careers = CareerPath.objects.all()
        if domain_filter:
            careers = careers.filter(domain=domain_filter)
        if search_query:
            careers = careers.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(required_skills__icontains=search_query)
            )
        from .models import CAREER_DOMAIN_CHOICES
        context = {
            'careers': careers,
            'domain_choices': CAREER_DOMAIN_CHOICES,
            'selected_domain': domain_filter,
            'search_query': search_query,
        }
        return render(request, self.template_name, context)


class CareerDetailView(View):
    template_name = 'career_edu/career_detail.html'

    def get(self, request, pk):
        career = get_object_or_404(CareerPath, pk=pk)
        resources = career.resources.all()
        context = {
            'career': career,
            'resources': resources,
        }
        return render(request, self.template_name, context)


class EducationResourcesView(View):
    template_name = 'career_edu/education_resources.html'

    def get(self, request):
        domain_filter = request.GET.get('domain', '')
        resource_type_filter = request.GET.get('type', '')
        difficulty_filter = request.GET.get('difficulty', '')
        search_query = request.GET.get('q', '')
        free_only = request.GET.get('free', '')

        resources = EducationResource.objects.all()
        if domain_filter:
            resources = resources.filter(domain=domain_filter)
        if resource_type_filter:
            resources = resources.filter(resource_type=resource_type_filter)
        if difficulty_filter:
            resources = resources.filter(difficulty=difficulty_filter)
        if free_only:
            resources = resources.filter(is_free=True)
        if search_query:
            resources = resources.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(skills_covered__icontains=search_query) |
                Q(provider__icontains=search_query)
            )

        from .models import CAREER_DOMAIN_CHOICES, RESOURCE_TYPE_CHOICES, DIFFICULTY_CHOICES
        context = {
            'resources': resources,
            'domain_choices': CAREER_DOMAIN_CHOICES,
            'resource_type_choices': RESOURCE_TYPE_CHOICES,
            'difficulty_choices': DIFFICULTY_CHOICES,
            'selected_domain': domain_filter,
            'selected_type': resource_type_filter,
            'selected_difficulty': difficulty_filter,
            'search_query': search_query,
            'free_only': free_only,
        }
        return render(request, self.template_name, context)


class ProfileView(LoginRequiredMixin, View):
    template_name = 'career_edu/profile.html'
    login_url = 'login'

    def get(self, request):
        profile = get_or_create_profile(request.user)
        form = UserProfileForm(instance=profile)
        context = {'form': form, 'profile': profile}
        return render(request, self.template_name, context)

    def post(self, request):
        profile = get_or_create_profile(request.user)
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('career-dashboard')
        context = {'form': form, 'profile': profile}
        return render(request, self.template_name, context)
