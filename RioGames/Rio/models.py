from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_by = models.ForeignKey(User,related_name='categories', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Category/',null=True)

    def __str__(self):
        return self.name

class Element(models.Model):
    name = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Category,related_name='elements', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Elements/',null=True)
    son = models.FileField( upload_to='SoundName/' , max_length=100,null=True)
    def __str__(self):
        return self.name

class Comments(models.Model):
    message = models.TextField(max_length=4000)
    email = models.EmailField(max_length=254)
    name = models.CharField(max_length=50)
    time = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.name

class ImgConvert(models.Model):
    CartonImg = models.ImageField(upload_to='ConvertImg/',null=True)
    EdgeImg = models.ImageField(upload_to='ConvertImg/',null=True)
    def __str__(self):
        return self.name

class Quiz(models.Model):
    image_El = models.ImageField(upload_to='ElementsQuiz/',null=True)
    category = models.ForeignKey(Category,related_name='quiz', on_delete=models.CASCADE,null=True)
    val_correct =models.CharField(max_length=50,null=True)
    val_fause1=models.CharField(max_length=50, null=True)
    val_fause2=models.CharField(max_length=50, null=True)
    val_fause3=models.CharField(max_length=50, null=True)
    son = models.FileField( upload_to='Sound/' , max_length=100,null=True)
    def __str__(self):
        return self.val_correct