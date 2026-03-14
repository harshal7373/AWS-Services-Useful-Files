from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('career/', include('career_edu.urls')),
    path('', include('employee_app.urls')),
]


