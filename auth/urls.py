from django.urls import path,include
from django.contrib.auth import views as auth_views
# from django.urls import reverse_lazy
from auth import views

urlpatterns=[
    path('login',views.login,name='auth_login'),
    path('signup',views.signup),
    path('logout',views.auth_logout,name='auth_logout'),
    path('', include('allauth.urls')),
    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(success_url='done',template_name='resources/change-password.html'),
        name='change_password'
    ),

    path('change-password/done',auth_views.PasswordChangeDoneView.as_view(template_name='resources/password_change_done.html')),
]
