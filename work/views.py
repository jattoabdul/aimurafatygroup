from django.shortcuts import render, get_object_or_404
from work.models import Project
from django.shortcuts import redirect


# Create your views here.
def work(request):
    project = Project.objects.all()[:6]
    context_dict = {'gallery': project}
    return render(request, 'portfolio/portfolio.html', context=context_dict)
