from django.db import models
from django.contrib.auth.models import User


EDUCATION_LEVEL_CHOICES = [
    ('high_school', 'High School'),
    ('diploma', 'Diploma'),
    ('bachelors', "Bachelor's Degree"),
    ('masters', "Master's Degree"),
    ('phd', 'PhD'),
    ('other', 'Other'),
]

EXPERIENCE_CHOICES = [
    ('student', 'Student'),
    ('fresher', 'Fresher (0-1 years)'),
    ('junior', 'Junior (1-3 years)'),
    ('mid', 'Mid-Level (3-6 years)'),
    ('senior', 'Senior (6+ years)'),
]

CAREER_DOMAIN_CHOICES = [
    ('technology', 'Technology'),
    ('business', 'Business & Management'),
    ('healthcare', 'Healthcare'),
    ('arts', 'Arts & Design'),
    ('science', 'Science & Research'),
    ('education', 'Education & Teaching'),
    ('finance', 'Finance & Accounting'),
    ('law', 'Law & Legal'),
    ('engineering', 'Engineering'),
    ('marketing', 'Marketing & Communication'),
]

RESOURCE_TYPE_CHOICES = [
    ('course', 'Online Course'),
    ('book', 'Book'),
    ('video', 'Video Tutorial'),
    ('article', 'Article / Blog'),
    ('certification', 'Certification'),
    ('workshop', 'Workshop'),
]

DIFFICULTY_CHOICES = [
    ('beginner', 'Beginner'),
    ('intermediate', 'Intermediate'),
    ('advanced', 'Advanced'),
]


class CareerPath(models.Model):
    title = models.CharField(max_length=100)
    domain = models.CharField(max_length=30, choices=CAREER_DOMAIN_CHOICES)
    description = models.TextField()
    required_skills = models.TextField(help_text='Comma-separated list of skills')
    avg_salary = models.CharField(max_length=50)
    growth_outlook = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, default='briefcase')

    def __str__(self):
        return self.title

    def skills_list(self):
        return [s.strip() for s in self.required_skills.split(',') if s.strip()]


class EducationResource(models.Model):
    title = models.CharField(max_length=200)
    provider = models.CharField(max_length=100)
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPE_CHOICES)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    domain = models.CharField(max_length=30, choices=CAREER_DOMAIN_CHOICES)
    career_paths = models.ManyToManyField(CareerPath, blank=True, related_name='resources')
    description = models.TextField()
    url = models.URLField(blank=True, default='')
    duration = models.CharField(max_length=50, blank=True, default='')
    is_free = models.BooleanField(default=True)
    skills_covered = models.TextField(help_text='Comma-separated list of skills', blank=True, default='')

    def __str__(self):
        return self.title

    def skills_list(self):
        return [s.strip() for s in self.skills_covered.split(',') if s.strip()]


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='career_profile')
    education_level = models.CharField(max_length=20, choices=EDUCATION_LEVEL_CHOICES, blank=True, default='')
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, blank=True, default='student')
    current_skills = models.TextField(blank=True, default='', help_text='Comma-separated list of your current skills')
    interests = models.ManyToManyField(CareerPath, blank=True, related_name='interested_users')
    bio = models.TextField(blank=True, default='')
    target_role = models.CharField(max_length=100, blank=True, default='')
    linkedin_url = models.URLField(blank=True, default='')
    github_url = models.URLField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def skills_list(self):
        return [s.strip() for s in self.current_skills.split(',') if s.strip()]

    def get_recommended_resources(self):
        user_skills = set(s.lower() for s in self.skills_list())
        interested_domains = self.interests.values_list('domain', flat=True)
        resources = EducationResource.objects.filter(domain__in=interested_domains)
        if not resources.exists():
            resources = EducationResource.objects.all()
        return resources[:6]

    def get_recommended_careers(self):
        if self.interests.exists():
            return self.interests.all()[:4]
        return CareerPath.objects.all()[:4]
