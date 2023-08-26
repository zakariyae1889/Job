from django_filters import FilterSet
from .models import Job
class JobFilter(FilterSet):
    class Meta:
        model=Job
        fields=['Category','Jobtype']