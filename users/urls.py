from django.urls import path
from .views import signup_view, home_view
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('', home_view, name='home'),  # Set '' as the default home page
    path('home/', home_view, name='home'),  # Keep '/home/' in case it's referenced elsewhere
    path('translate_text/', views.translate_text, name='translate_text'),    
    path('quizzes/', views.quiz_page, name='quiz_page'),
    path('quiz/<str:quiz_name>/', views.start_quiz, name='start_quiz'),
    path('quiz/submit/', views.submit_quiz, name='submit_quiz'),

    

]
