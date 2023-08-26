from django.shortcuts import render
from JobsApp.models import Job
# Create your views here.
class HomeApp():
    def PageHome(request):
        job=Job.objects.all()[0:4]
        return render(request,template_name='Home.html',context=
        {
            "job":job
            
        })