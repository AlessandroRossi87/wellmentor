# pylint: disable=E1101
from django.shortcuts import render
from django.views import generic

# Create your views here.
class SurveyView(generic.View):
  """BASIC VIEW FOR SURVEY PAGE"""

  def get(self, request, *args, **kwargs):
        return render(request, "survey/survey.html")


class SurveyResultsView(generic.View):
  """BASIC VIEW FOR SURVEY RESULTS PAGE"""

  def get(self, request, *args, **kwargs):
        return render(request, "survey/results.html")


class AboutUsView(generic.View):
  """BASIC VIEW FOR SURVEY RESULTS PAGE"""

  def get(self, request, *args, **kwargs):
        return render(request, "survey/about_us.html")


class HomePageView(generic.View):
  """BASIC VIEW FOR SURVEY PAGE"""

  def get(self, request, *args, **kwargs):
        return render(request, "survey/home.html")
