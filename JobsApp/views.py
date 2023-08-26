from django.shortcuts import render,get_object_or_404,redirect
from .filters import JobFilter
from .models import Job
from  django.core.paginator import Paginator
from .form import ApplyJobForm,PostJobForm
from django.contrib import messages

from django.contrib.auth.decorators import login_required

class JobApp():
    #----------------------------------------------------------#
    def PageJob(request):
        job=Job.objects.all()
        #------------Filter Job-----#
        myfilter=JobFilter(request.GET,queryset=job)
        job=myfilter.qs
        #-----Paginator-------------#
        paginator=Paginator(job,6)
        PageNumber=request.GET.get('page')
        Page_obj=paginator.get_page(PageNumber)
        
        return render(request,template_name='Job/browsejobs.html',context={
            "job":Page_obj,
            "myfilter":myfilter
        })
    #----------------------------------------------------------------#
    def PageSingle(request,Slug):
        job_single=get_object_or_404(Job,slug=Slug)
        if request.method=="POST":
            
            FormApply=ApplyJobForm(request.POST,request.FILES)
            if FormApply.is_valid():
                myform=FormApply.save(commit=False)
                myform.Jobs=job_single
                myform.save()
                messages.success(request,"Job Apply Successfluy")
            else:  messages.error(request,'error')
        else:FormApply=ApplyJobForm()
        return render(request,template_name='Job/single-job.html',context={
        'job_single':job_single,
        "FormApply":FormApply,
    })
    @login_required(login_url='Login')
    def PagePostJob(request):
        if request.method=="POST":
            formJob=PostJobForm(request.POST)
            if  formJob.is_valid():
                myform=formJob.save(commit=False)
                myform.Owner=request.user
                myform.save()
                messages.success(request,"Job Post Successfluy")
                return redirect("job")
            else:messages.error(request,'error')
        else: formJob=PostJobForm()
        return render(request,template_name='Job/job-post.html', context={
        "formJob": formJob
    })

    

