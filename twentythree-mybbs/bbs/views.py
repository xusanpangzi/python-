from django.shortcuts import render
from bbs import models
import time
# Create your views here.
def index(request):
    if request.method=="POST":
        username=request.POST.get("name",None)
        sentence=request.POST.get("txt",None)
        t=time.localtime()
        T=time.strftime("%Y-%m-%d %H:%M:%S",t)
        models.UserInfo.objects.create(user=username,word=sentence,Time=T)
    user_list=models.UserInfo.objects.all()
    return render(request,"index.html",{"data":user_list})
