from django.contrib import admin
from .models import CareerPath, EducationResource, UserProfile


@admin.register(CareerPath)
class CareerPathAdmin(admin.ModelAdmin):
    list_display = ('title', 'domain', 'avg_salary', 'growth_outlook')
    list_filter = ('domain',)
    search_fields = ('title', 'description', 'required_skills')


@admin.register(EducationResource)
class EducationResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'provider', 'resource_type', 'difficulty', 'domain', 'is_free')
    list_filter = ('resource_type', 'difficulty', 'domain', 'is_free')
    search_fields = ('title', 'description', 'provider', 'skills_covered')
    filter_horizontal = ('career_paths',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'education_level', 'experience_level', 'target_role')
    list_filter = ('education_level', 'experience_level')
    search_fields = ('user__username', 'target_role', 'current_skills')
    filter_horizontal = ('interests',)
