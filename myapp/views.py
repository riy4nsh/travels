from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.context_processors import request

from myapp.models import registertbl, contacttbl, logintbl


# Create your views here.
def index(request):
    return render(request,"index.html")
def tours(request):
    return render(request,"tours.html")
def destinations(request):
    return render(request,"destinations.html")
def news(request):
    return render(request,"news.html")
def contact(request):
    return render(request,"contact.html")
def about(request):
    return render(request,"about.html")
def login(request):
    return render(request,"login.html")
def register(request):
    return render(request,"register.html")
def admin(request):
    return render(request,"admin.html")

def reg(request):
    y1=1
    res=registertbl.objects.all()
    return render(request,"reg.html",{"result":res,"y":y1})


def log(request):
    return render(request,"log.html")


def cont(request):
    res = contacttbl.objects.all()
    return render(request, "cont.html", {"result": res})


def admin_login(request):
    return render(request,"admin_login.html")




def delete(request,id):
    dell=registertbl.objects.get(id=id)
    dell.delete()
    return redirect("../reg")



def deletedata(request,id):
    dell=contacttbl.objects.get(id=id)
    dell.delete()
    return redirect("../cont")





def formcode(request):
    a=request.POST['name']
    b=request.POST['email']
    c=request.POST['phone']
    d=request.POST['password']
    e=request.POST['repeatpassword']

    # Validate password match
    if d != e:
        return render(request, 'register.html', {'error': 'Passwords do not match'})

    # Save data to the database
    ins = registertbl(name=a, email=b, phone=c, password=d, repeatpassword=e)
    ins.save()

    # Return to the same page but with a success message
    return render(request, 'register.html', {'success': True})


    return render(request, 'register.html')


def contact(request):
    return render(request,"contact.html")


def signupcode(request):
    a=request.POST['name']
    b=request.POST['email']
    c=request.POST['number']
    d=request.POST['message']
    ins=contacttbl(name=a,email=b,number=c,message=d)
    ins.save()
    # Save data to the database
    ins = contacttbl(name=a, email=b, number=c, message=d)
    ins.save()

    # Redirect to the same page but set a success flag
    return HttpResponseRedirect('../contact?success=true')


def edit(request,id):
    ed=registertbl.objects.get(id=id)
    return render(request,"edit.html",{"res":ed})

def update(request):
    a=request.POST['id']
    b=request.POST['name']
    c=request.POST['email']
    d=request.POST['phone']
    e=request.POST['password']
    f=request.POST['repeatpassword']
    up=registertbl.objects.filter(id=a).update(name=b,email=c,phone=d,password=e,repeatpassword=f)
    return redirect("../reg")


def editdata(request,id):
    ed=contacttbl.objects.get(id=id)
    return render(request,"editdata.html",{"res":ed})

def updatecode(request):
    a=request.POST['id']
    b=request.POST['name']
    c=request.POST['email']
    d=request.POST['number']
    e=request.POST['message']
    up=contacttbl.objects.filter(id=a).update(name=b,email=c,number=d,message=d)
    return redirect("../cont")


def logincode(request):
    a=request.POST['email']
    b=request.POST['password']
    if registertbl.objects.filter(email=a).exists():
        if registertbl.objects.filter(password=b).exists():
            return HttpResponseRedirect("../index")
        else:
            return HttpResponse("wrong password")
    else:
        return HttpResponse("wrong email")

def login(request):
    return render(request,"login.html")


def adminlogin(request):
    return render(request,"admin_login.html")



def logcode(request):
    a=request.POST['email']
    b=request.POST['password']
    if logintbl.objects.filter(email=a).exists():
        if logintbl.objects.filter(password=b).exists():
            return HttpResponseRedirect("../admins")
        else:
            return HttpResponse("wrong password")
    else:
        return HttpResponse("wrong email")

