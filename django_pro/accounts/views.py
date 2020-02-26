from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout
from django.http import HttpResponse
from .models import Captcha
from PIL import Image,ImageDraw,ImageFont
import random
import operator
# Create your views here.
def signup_view(request):
    cap = request.POST.get('captcha')
    obj = [str(cap.captcha) for cap in Captcha.objects.all()]
    print(obj)
    print(str(cap)==obj[0])

    if request.method == 'POST':
        print('cap',cap)
        if str(cap) != obj[0]:
            return HttpResponse('<html><script>alert("Enter valid amount");window.location="http://127.0.0.1:8000/accounts/signup/";</script></html>')
        form1 = UserCreationForm(request.POST)
        if form1.is_valid():
            user = form1.save()
            login(request,user)
            return redirect('articles:list')
    else:
        res = text_on_img(size=300)
        t = Captcha.objects.get(id=1)
        t.captcha = str(res)
        t.save()
        print('res',res)
        form1 = UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form1})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

def text_on_img(filename=r'\01.png',size=12):
    opers = ['+', '-', '/', '*']
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    n1,n2 = random.randint(1, 20),random.randint(1, 5)
    opr = opers[random.randint(0, len(opers) - 1)]
    res = ops[opr](n1,n2)
    fnt = ImageFont.truetype('arial.ttf',size)
    text = str(n1) + ' ' + opr + ' ' + str(n2)
    image = Image.new(mode='RGB',size=(int(size/2)*len(text),size+50),color='blue')
    draw = ImageDraw.Draw(image)
    draw.text((10,10),text,font=fnt,fill=(255,255,0))
    filename = r'C:\sem-3\itws - 3\project\django_project\django_pro\static' + filename
    image.save(filename)
    return res

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:login')
