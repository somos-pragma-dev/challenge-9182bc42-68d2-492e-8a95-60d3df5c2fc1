urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
]


from django.contrib import admin
from.models import UserProfile