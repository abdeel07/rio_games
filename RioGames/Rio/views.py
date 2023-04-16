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
        comment = Comments()
        
        comment.name = query.POST['Nom']
        comment.email = query.POST['email']
        comment.message = query.POST['message']
        comment.time = datetime.now()
        
        comment.save()
        
        return redirect('HomePage')
    
    category = Category.objects.all()
    return render(query,'Home.html',{'Cat':category})

def Elements(query, Category_id):
    category = Category.objects.filter(pk=Category_id)
    element = Element.objects.all().filter(category=Category_id)
    
    return render(query,'Elements.html',{'elem':element, 'ca':category})

@login_required
def Moderateur(query):
    if query.user.is_authenticated:
        moderateur = User.objects.get(pk=query.user.pk)
        return render(query,'ModerateurHome.html',{'user':moderateur})
    
@login_required
def AjouterCat(query, moderateurId):
    if query.method == 'POST':
        Cat = Category()
        Cat.name = query.POST['nom']
        Cat.image = query.FILES['image']
        Cat.created_by = User.objects.get(pk=query.POST['id'])
        Cat.save()
        
    moderateur = User.objects.get(pk=moderateurId)
    
    return render(query,'AjouterCat.html',{'user':moderateur})

@login_required
def AjouterElem(query, moderateurId):
    if query.method == 'POST':
        element = Element()
        
        element.name = query.POST['nom']
        element.image = query.FILES['image']
        element.son = query.FILES['son']
        element.category = Category.objects.get(pk=query.POST['cat'])
        
        element.save()
        
    moderateur = User.objects.get(pk=moderateurId)
    category = Category.objects.all().filter(created_by=moderateurId)
    
    return render(query,'AjouterElem.html',{'user':moderateur, 'cat':category})


def Quiz(query,Category_id):
    all_quiz=Qw.objects.all().filter(category=Category_id)

    T = list(all_quiz)
    random.shuffle(T)
    return render(query,'Quiz.html',{'all_quiz':T})

def Conimg(query):
    if query.method == 'POST':
        img = query.FILES['img']

        fileSystem = FileSystemStorage()
        I = fileSystem.save(img.name, img)
        url = fileSystem.url(I)
        
        Convert("." + url)
    
    return render(query,'ConvertImg.html')
    
def Jeux(query):
    return render(query,'Jeux.html')

def JeuxHome(query):
    return render(query,'JeuxHome.html')


def Comment(query):
    comment = Comments.objects.all()
    return render(query,'Comment.html',{'com':comment})

def Convert(img):
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
    
    imgConvert = ImgConvert.objects.create(
            CartonImg = "ConvertImg/ImgCartoon.png",
            EdgeImg = "ConvertImg/ImgEdges.png",
        )