from django import forms
from .models import UserProfile, EDUCATION_LEVEL_CHOICES, EXPERIENCE_CHOICES


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['education_level', 'experience_level', 'current_skills', 'bio',
                  'target_role', 'linkedin_url', 'github_url', 'interests']
        labels = {
            'education_level': 'Highest Education Level',
            'experience_level': 'Experience Level',
            'current_skills': 'Current Skills',
            'bio': 'About Me',
            'target_role': 'Target Role / Dream Job',
            'linkedin_url': 'LinkedIn Profile URL',
            'github_url': 'GitHub Profile URL',
            'interests': 'Career Interests',
        }
        widgets = {
            'current_skills': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'e.g. Python, JavaScript, Communication, Problem Solving'
            }),
            'bio': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Tell us a bit about yourself and your career goals...'
            }),
            'target_role': forms.TextInput(attrs={
                'placeholder': 'e.g. Full Stack Developer, Data Scientist, Product Manager'
            }),
            'interests': forms.CheckboxSelectMultiple(),
        }
