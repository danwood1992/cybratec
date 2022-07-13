from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    page = 'projects'
    number = 10
    context = {'page': page, 'number': number}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    page = 'single project'
    return render(request, 'projects/single-project.html', {'page':page})
    
    
    


#return HttpResponse('hi im project' + ' ' + str(pk))

