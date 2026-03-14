from django.urls import path
from .views import (
    CareerHomeView, DashboardView, CareerExploreView,
    CareerDetailView, EducationResourcesView, ProfileView
)

urlpatterns = [
    path('', CareerHomeView.as_view(), name='career-home'),
    path('dashboard/', DashboardView.as_view(), name='career-dashboard'),
    path('careers/', CareerExploreView.as_view(), name='career-explore'),
    path('careers/<int:pk>/', CareerDetailView.as_view(), name='career-detail'),
    path('resources/', EducationResourcesView.as_view(), name='education-resources'),
    path('profile/', ProfileView.as_view(), name='career-profile'),
]
