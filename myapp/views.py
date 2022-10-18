from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Feature
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

# def index(requset):
#     return HttpResponse('<h1>Hey,Welcome</h1>')

# def index(request):
#     context = {
#         'name':'Amm',
#         'age': 10, 
#         'nationality':'Laos'
#     }
#     return render(request, 'index.html',context) 

# def index(request):
#     feature1 = Feature()
#     feature1.id = 0
#     feature1.name = 'Naruto Uzumaki'
#     feature1.is_true = True
#     feature1.details = '(Japanese: うずまき ナルト, Hepburn: Uzumaki Naruto) (/ˈnɑːrətoʊ/) is the titular protagonist of the manga Naruto, created by Masashi Kishimoto. As the series progresses, he is a young ninja from the fictional village of Konohagakure (Hidden Leaf Village). '

#     feature2 = Feature()
#     feature2.id = 1
#     feature2.name = 'Kakashi Hatake'
#     feature2.is_true = True
#     feature2.details = '(Japanese: はたけ カカシ, Hepburn: Hatake Kakashi) is a fictional character in the Naruto manga and anime series created by Masashi Kishimoto. In the story, Kakashi is the teacher of Team 7,'

#     feature3 = Feature()
#     feature3.id = 2
#     feature3.name = 'Minato Namikaze'
#     feature3.is_true = False
#     feature3.details = 'Namikaze Minato was the Fourth Hokage (四代目火影, Yondaime Hokage, literally meaning: Fourth Fire Shadow) of Konohagakure. He was renowned all over the world as Konoha Yellow Flash'

#     feature4 = Feature()
#     feature4.id = 3
#     feature4.name = 'Shikamaru Nara'
#     feature4.is_true = False
#     feature4.details = 'is the one of main characters of the Naruto anime/manga series, and a supporting character in the Boruto: Naruto Next Generations anime/manga series both created by Masashi Kishimoto'

#     feature5 = Feature()
#     feature5.id = 4
#     feature5.name = 'Itachi'
#     feature5.is_true = True
#     feature5.details = ' is the older brother of Sasuke Uchiha, and is responsible for killing all the members of their clan, sparing only Sasuke.'

#     features = [feature1,feature2,feature3,feature4,feature5]

#     return render(request, 'index.html',{'features':features}) 


def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html',{'features':features})

def register(requset):
    if requset.method == 'POST':
        username = requset.POST['username']
        email = requset.POST['email']
        password = requset.POST['password']
        password2 = requset.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(requset, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(requset, 'Username Already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(requset, 'Password Not The Same')
            return redirect('register')
    else:
        return render(requset,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Credentials Invalid')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


# def counter(request):
#     # text = request.POST['text']
#     # amount_of_words = len(text.split())
#     # return render(request,'counter.html',{'amount':amount_of_words})

def counter(request):
    posts = [1,2,3,4,5,'amm','amm2','amm3']
    return render(request,'counter.html',{'posts':posts})

def post(request, pk): 
    return render(request,'post.html',{'pk': pk})