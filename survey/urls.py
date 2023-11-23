from django.urls import path
from . import views

urlpatterns = [
<<<<<<< Updated upstream
    path('', views.SurveyView.as_view(), name='survey'),
    path('/results', views.SurveyResultsView.as_view(), name='results'),
    path('/about-us', views.AboutUsView.as_view(), name='about_us'),
=======
    path('', views.HomePageView.as_view(), name='home'),
    path('survey', views.SurveyView.as_view(), name='survey'),
    path('results', views.SurveyResultsView.as_view(), name='results'),
    path('about-us', views.AboutUsView.as_view(), name='about_us'),
    path('accounts/profile/', views.HomePageView.as_view(), name='profile'), 
>>>>>>> Stashed changes
]
