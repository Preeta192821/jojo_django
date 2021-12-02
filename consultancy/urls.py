from django.urls import path
from .views import*

urlpatterns = [
    path('home', home, name='users-home'),
    path('',Index, name='users-index'),
    path('about',About, name='users-about'),
    path('contact',Contact, name='users-contact'),
    path('newregister/', RegisterView.as_view(), name='users-newregister'),
    path('profile/', profile, name='users-profile'),
    path('newlogin/',CustomLoginView.as_view(redirect_authenticated_user=True, template_name='users/newlogin.html',
                                           authentication_form=LoginForm), name='newlogin'),
]
