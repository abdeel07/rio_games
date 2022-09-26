from django.urls import path

from Rio import views

urlpatterns = [
    path('',views.Home,name='HomePage'),
    path('Element/<int:Category_id>',views.Elements,name='Element'),
    path('ConvertImg/',views.Conimg,name='convertImg'),
    path('ModerateurHome/',views.Moderateur,name='ModerateurHome'),
    path('AjouterCat/<int:MoId>',views.AjouterCat,name='AjouterCat'),
    path('AjouterElem/<int:MoId>',views.AjouterElem,name='AjouterElem'),
    path('Quiz/<int:Category_id>',views.Quiz,name='Quiz'),
    path('Jeux/',views.Jeux,name='Jeux'),
    path('JeuxHome/',views.JeuxHome,name='JeuxHome'),
    path('Comment/',views.Comment,name='Comment'),
]