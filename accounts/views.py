from django.shortcuts import render,get_object_or_404,redirect
from .form import SingUpForm,ProfileForm,UserForm
from django.contrib.auth import login ,authenticate
from django.contrib.auth.decorators import login_required
from .models import Profiles
from django.contrib.auth.models import User

class Accounts():
    def SingUpPages(request):
        if request.method=='POST':
           
            form =SingUpForm(request.POST,request.FILES)
            if form.is_valid() :
                form.save()
                username=form.cleaned_data['username']
                password=form.cleaned_data['password1']
                photo=form.cleaned_data["photo"]
                phone=form.cleaned_data["phone"]
                city=form.cleaned_data['city']
                country=form.cleaned_data['country']
                
                user=authenticate(username=username,password=password)
                pro=Profiles(users=user,Country=country,City=city,Photo=photo,Phone=phone)
                pro.save()
               
                login(request,user)
                return redirect("Profile")
            else:pass
        else:form=SingUpForm()
        return render(request,template_name='accounts/SingUp.html',context={
            'form':form
        })
    

    @login_required(login_url='Login')
    def PageProfile(request):
        pro=get_object_or_404(Profiles, users=request.user)
        return render(request,template_name='accounts/Profiles.html', context={"pro":pro})
    

    @login_required(login_url='Login')
    def  PageEditProfile(request):
        pro=get_object_or_404(Profiles,users=request.user)
        if request.method=="POST":
            userform=UserForm(request.POST,instance=request.user)
            profileform=ProfileForm(request.POST,request.FILES,instance=pro)
            if userform.is_valid and profileform.is_valid():
                userform.save()
                myprofile=profileform.save(commit=False)
                myprofile.users=request.user
                myprofile.save()
                return redirect("Profile")
        else:
            userform=UserForm(instance=request.user)
            profileform=ProfileForm(instance=pro)
        return render(request,template_name="accounts/Edit-Profile.html", context={
            'userform':userform,
            'profileform':profileform,
        })
    @login_required(login_url='Login')
    def PageDeleteAccount(request):
        
        pro=get_object_or_404(Profiles,users=request.user)
        user=User.objects.filter(username=pro)
        user.delete()
        return redirect("home")