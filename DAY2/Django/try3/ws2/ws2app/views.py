from django.shortcuts import render
from .models import Student

def index(request):
  num=Student.objects.all().count()
  s=Student.objects.all()
  sum=0
  avg=[]
  grade=[]
  for i in range(0,num):
      sum=0
      sum+=s[i].sub1_m+s[i].sub2_m+s[i].sub3_m
      avg.append(sum/3)
      if(avg[i]>=85):
        grade.append('A')
      elif(avg[i]>=65):
        grade.append('B')
      else:
        grade.append('C')
  report=zip(s,avg,grade)
  return render(request,'index.html',context={'numb':num,'avg':avg,'report':report})