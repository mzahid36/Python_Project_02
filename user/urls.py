from user import views
from django.urls import path

urlpatterns = [
    path('',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout')

]
