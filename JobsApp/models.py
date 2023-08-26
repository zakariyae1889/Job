from django.utils.text import slugify
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
typeJob=(
   ('Full Time','Full Time'),
   ('Part Time','Part Time'),
   ('Freelance','Freelance'),
   ("Internship","Internship"),
   ('Termporary','Termporary')
)
class  Categories(models.Model):
    name=models.CharField(max_length=355)
    def __str__(self) -> str:
       return self.name

class Job(models.Model):
  
  Category=models.ForeignKey(Categories,on_delete=models.CASCADE)
  Owner=models.ForeignKey(User,on_delete=models.CASCADE)
  Title=models.CharField(max_length=255)
  
  Company=models.CharField(max_length=255)
  EmailAddress=models.EmailField(unique=True)
  Location=models.CharField(max_length=255)
  Price=models.PositiveBigIntegerField()
  Jobtype=models.CharField(max_length=255,choices=typeJob)
  Vacancy=models.PositiveIntegerField(default=0)
  Experiencse=models.PositiveIntegerField(default=0)
  Description=models.TextField()
  
  slug=models.SlugField(blank=True,null=True)
  Pulished_at=models.DateTimeField(auto_now=True)


  def save(self,*args,**Kwargs):
    self.slug=slugify(self.Title) 
    return super(Job,self).save(*args,**Kwargs)
  

  def __str__(self) -> str:
     return self.Title
  
class ApplyJob(models.Model):
   Name=models.CharField(max_length=255)
   Email=models.EmailField(unique=True)
   Jobs=models.ForeignKey(Job,on_delete=models.CASCADE)
   CV=models.FileField()
   CoverLetter=models.TextField()
   create_at=models.DateTimeField(auto_now=True)

   def __str__(self) -> str:
      return self.Name




