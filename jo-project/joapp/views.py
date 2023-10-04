from django.shortcuts import render
from .models import place,team
# Create your views here.
def index(request):
    obj = place.objects.all()
    teams = team.objects.all()
    return render(request,'index.html',{'obj':obj,'teams':teams})