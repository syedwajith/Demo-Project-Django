from django.shortcuts import render,HttpResponse,redirect
from firstapp.models import registerdetails

# Create your views here.

def registerpage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        username = request.POST.get('username')
        password = request.POST.get('password')
        users = registerdetails()
        users.Name = name
        users.Address = address
        users.Username = username
        users.Password = password
        users.save()
    return render(request, 'firstapp/register.html')

def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            registerdetails.objects.get(Username=username)
            return HttpResponse('welcome user')
        except:
            registerdetails.objects.get(Password=password)
            return HttpResponse('Invalid user')
    return render(request, 'firstapp/login.html')

def adminlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'admin' and password == 'admin':
            return HttpResponse('Welcome Admin')
        else:
            return HttpResponse('Invalid')
    return render(request, 'firstapp/adminlogin.html')

def pending(request):
    details = registerdetails.objects.filter(Status=False)
    return render(request, 'firstapp/pendinglist.html',{'value':details})

def approved(request):
    details = registerdetails.objects.filter(Status=True)
    return render(request,'firstapp/approvedlist.html',{'value':details})

def approve(request,id):
    data = registerdetails.objects.get(id=id)
    data.Status = True
    data.save()
    return redirect('/firstapp/pending')

def edit(request,id):
    details = registerdetails.objects.filter(Status=True)
    users = registerdetails.objects.get(id=id)
    if request.method == 'POST':
        address = request.POST.get('address')
        password = request.POST.get('password')
        users.Address = address
        users.Password = password
        users.save()
        return redirect('/firstapp/approved')
    return render(request, 'firstapp/approvedlist.html',{'value':details,'a':users})

def delete(request,id):
    data = registerdetails.objects.filter(id=id).delete()
    return redirect('/firstapp/approved')