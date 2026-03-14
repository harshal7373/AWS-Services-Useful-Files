from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import CareerPath, EducationResource, UserProfile


class CareerPathModelTest(TestCase):
    def setUp(self):
        self.career = CareerPath.objects.create(
            title='Software Engineer',
            domain='technology',
            description='Build software.',
            required_skills='Python, JavaScript, Git',
            avg_salary='$90,000 - $150,000',
            growth_outlook='Very High',
            icon='code-slash',
        )

    def test_career_str(self):
        self.assertEqual(str(self.career), 'Software Engineer')

    def test_skills_list(self):
        skills = self.career.skills_list()
        self.assertEqual(skills, ['Python', 'JavaScript', 'Git'])


class EducationResourceModelTest(TestCase):
    def setUp(self):
        self.resource = EducationResource.objects.create(
            title='Python Course',
            provider='Udemy',
            resource_type='course',
            difficulty='beginner',
            domain='technology',
            description='Learn Python.',
            is_free=False,
            skills_covered='Python, OOP',
        )

    def test_resource_str(self):
        self.assertEqual(str(self.resource), 'Python Course')

    def test_skills_list(self):
        skills = self.resource.skills_list()
        self.assertIn('Python', skills)


class CareerHomeViewTest(TestCase):
    def test_home_page_loads(self):
        response = self.client.get(reverse('career-home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'CareerPath')

    def test_home_shows_careers(self):
        CareerPath.objects.create(
            title='Data Scientist', domain='technology',
            description='Analyze data.', required_skills='Python, SQL',
            avg_salary='$100,000', growth_outlook='High', icon='graph-up',
        )
        response = self.client.get(reverse('career-home'))
        self.assertContains(response, 'Data Scientist')


class CareerExploreViewTest(TestCase):
    def setUp(self):
        CareerPath.objects.create(
            title='Cloud Architect', domain='technology',
            description='Design cloud solutions.', required_skills='AWS, Azure',
            avg_salary='$130,000', growth_outlook='High', icon='cloud',
        )

    def test_explore_page_loads(self):
        response = self.client.get(reverse('career-explore'))
        self.assertEqual(response.status_code, 200)

    def test_search_filter(self):
        response = self.client.get(reverse('career-explore'), {'q': 'Cloud'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Cloud Architect')

    def test_domain_filter(self):
        response = self.client.get(reverse('career-explore'), {'domain': 'technology'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Cloud Architect')


class EducationResourcesViewTest(TestCase):
    def test_resources_page_loads(self):
        response = self.client.get(reverse('education-resources'))
        self.assertEqual(response.status_code, 200)

    def test_free_filter(self):
        EducationResource.objects.create(
            title='Free Course', provider='edX', resource_type='course',
            difficulty='beginner', domain='technology',
            description='Free resource.', is_free=True,
        )
        EducationResource.objects.create(
            title='Paid Course', provider='Udemy', resource_type='course',
            difficulty='beginner', domain='technology',
            description='Paid resource.', is_free=False,
        )
        response = self.client.get(reverse('education-resources'), {'free': '1'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Free Course')
        self.assertNotContains(response, 'Paid Course')


class ProfileViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser', password='testpass123')
        self.client.login(username='testuser', password='testpass123')

    def test_profile_page_loads(self):
        response = self.client.get(reverse('career-profile'))
        self.assertEqual(response.status_code, 200)

    def test_profile_redirects_for_anonymous(self):
        self.client.logout()
        response = self.client.get(reverse('career-profile'))
        self.assertEqual(response.status_code, 302)

    def test_profile_created_on_access(self):
        self.client.get(reverse('career-profile'))
        self.assertTrue(UserProfile.objects.filter(user=self.user).exists())


class DashboardViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('dashuser', password='testpass123')
        self.client.login(username='dashuser', password='testpass123')

    def test_dashboard_loads(self):
        response = self.client.get(reverse('career-dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'dashuser')

    def test_dashboard_redirects_for_anonymous(self):
        self.client.logout()
        response = self.client.get(reverse('career-dashboard'))
        self.assertEqual(response.status_code, 302)
