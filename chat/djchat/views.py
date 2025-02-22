from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib import messages
from djchat.models import room, message,signup
from django.http import HttpResponse,JsonResponse





# Create your views here.
def house(request):
    return render(request, 'house.html')





def signup(request):
   if  request.method=='POST':
        username=request.POST['username']
        
        password=request.POST['password']

        if signup.objects.filter(username=username).exists():
            messages.info(request,'username taken')
            return redirect('signup')
        
        else:
            user=signup.objects.create(username=username,password=password)
            user.save()
            return redirect('signin')
        
   else:
        return render(request, 'signup.html')
  
  

def rom(request, room_name):
    username=request.GET.get('username')
    room_details=room.objects.get(name=room_name)
    return render(request, 'rom.html', {'username': username,'room_details': room_details,'room_name': room_name})

def checkview(request):
    roomname=request.POST['room_name']
    user=request.POST['username']
    
    if room.objects.filter(name=roomname).exists():
        return redirect('/'+roomname+'/?username='+user)
    else:
     new_room=room.objects.create(name=roomname)
     new_room.save()
     return redirect('/'+roomname+'/?username='+user)

def send(request):
    username=request.POST['username']
    roomname=request.POST['roomname']
    messages=request.POST['message']
    new_message=message.objects.create(value=messages,user=username,room=roomname)
    new_message.save()
    return HttpResponse('message sent successfully')

def get_messages(request, room_name):
    room_details=room.objects.get(name=room_name)
    messages = message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})


def signin(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']   
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/house')
        else:
            messages.info(request,'invalid credentials')    
            return redirect('signin')
    else:
      return render(request, 'signin.html')