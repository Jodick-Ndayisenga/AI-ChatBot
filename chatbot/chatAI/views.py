from django.shortcuts import render,redirect
from django.http import JsonResponse
import openai
from django.contrib import auth
from django.contrib.auth.models import User
from django.utils import timezone
import random
from .models import Chats
openai_Secret_key = "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"

openai.api_key = openai_Secret_key

def getTitle(text:str) -> str:
    if len(text) <= 30:
        title = text

    elif len(text) >= 31:
        last = random.randint(27, 35)
        title = text[:last]
        title += "..."
    else:
        text = "What is your question?"
    return title



def askOpenAI(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content":message},
        ]
    )
    answer = response.choices[0].message.content.strip()
    return answer

def index(request):
    return render(request, 'login.html')

def chat(request):
    all_chats = Chats.objects.filter(user=request.user).order_by("-created_time")
    return render(request, 'chat.html',{"chats": all_chats[:3][::-1]})

def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = askOpenAI(message)
        title = getTitle(message)
        chat = Chats(user = request.user, message = message, response = response, created_time = timezone.now())
        chat.save()
        
        return JsonResponse({
            "message": message,
            "response": response,
            "title":title
        })
    
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save()
                auth.login(request, user)
                return redirect('login')
            except:
                error_message = 'Error creating account'
                return render(request, 'register.html', {'error_message': error_message})
        else:
            error_message = 'Password dont match'
            return render(request, 'register.html', {'error_message': error_message})
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request,username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("chat")
            
        else:
            error_message="Invalid user name or password!"
            return render(request, "login.html",{
                "error_message":error_message,
            })
    else:
        return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect('login')