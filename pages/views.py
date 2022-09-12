from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required

class HomePageView(TemplateView):
    template_name = 'home.html'


@login_required
def profile(request):
    return render(request, 'pages/profile.html')
    