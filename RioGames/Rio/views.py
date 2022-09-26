from datetime import datetime
import random
from django.shortcuts import get_object_or_404, render,redirect,get_list_or_404
from .models import Category,Element,Comments,ImgConvert,Quiz as Qw
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
import cv2
import numpy as np
from django.core.files.storage import FileSystemStorage

def Home(query):
    if query.method == 'POST':
        nom = query.POST['Nom']
        mail = query.POST['email']
        msg = query.POST['message']
        t = datetime.now()
        Cmt = Comments.objects.create(
            name = nom,
            email = mail,
            message = msg,
            time = t
        )
        return redirect('HomePage')
    
    category = Category.objects.all()
    return render(query,'Home.html',{'Cat':category})

def Elements(query,Category_id):
    ca = Category.objects.filter(pk=Category_id)
    Elem = Element.objects.all().filter(category=Category_id)
    return render(query,'Elements.html',{'elem':Elem,'ca':ca})

@login_required
def Moderateur(query):
    if query.user.is_authenticated:
        Mod = User.objects.get(pk=query.user.pk)
        return render(query,'ModerateurHome.html',{'user':Mod})
    
@login_required
def AjouterCat(query,MoId):
    if query.method == 'POST':
        Cat = Category()
        Cat.name = query.POST['nom']
        Cat.image = query.FILES['image']
        Cat.created_by = User.objects.get(pk=query.POST['id'])
        Cat.save()
    Mod = User.objects.get(pk=MoId)
    return render(query,'AjouterCat.html',{'user':Mod})

@login_required
def AjouterElem(query,MoId):
    if query.method == 'POST':
        Ele = Element()
        Ele.name = query.POST['nom']
        Ele.image = query.FILES['image']
        Ele.son = query.FILES['son']
        Ele.category = Category.objects.get(pk=query.POST['cat'])
        Ele.save()
    Mod = User.objects.get(pk=MoId)
    cat = Category.objects.all().filter(created_by=MoId)
    return render(query,'AjouterElem.html',{'user':Mod,'cat':cat})


def Quiz(query,Category_id):
    all_quiz=Qw.objects.all().filter(category=Category_id)

    T = list(all_quiz)
    random.shuffle(T)
    return render(query,'Quiz.html',{'all_quiz':T})

def Conimg(q):
    if q.method == 'POST':
        im = q.FILES['img']

        fs = FileSystemStorage()
        I = fs.save(im.name, im)
        url = fs.url(I)
        st="."+url
        Cv(st)
    
    return render(q,'ConvertImg.html')
    
def Jeux(q):
    return render(q,'Jeux.html')

def JeuxHome(q):
    return render(q,'JeuxHome.html')


def Comment(q):
    com = Comments.objects.all()
    return render(q,'Comment.html',{'com':com})

def Cv(img):
    image = cv2.imread(img)

    # Edges
    grey_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    invert = cv2.medianBlur(grey_img,5)
    sketch = cv2.adaptiveThreshold(invert, 255,
                cv2.ADAPTIVE_THRESH_MEAN_C,
                cv2.THRESH_BINARY, 9, 9)
    
    # Cartoonization
    color = cv2.bilateralFilter(image, 9, 100, 250)
    cartoon = cv2.bitwise_and(color, color, mask=sketch)
    
    print(cartoon)
    #cv2.imshow("Cartoon", cartoon)
    #cv2.imshow("edges", sketch)
    cv2.imwrite("./images/ConvertImg/ImgCartoon.png", cartoon)
    cv2.imwrite("./images/ConvertImg/ImgEdges.png", sketch)
    Cmt = ImgConvert.objects.create(
            CartonImg = "ConvertImg/ImgCartoon.png",
            EdgeImg = "ConvertImg/ImgEdges.png",
        )