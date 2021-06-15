from django.contrib import admin
from django.urls import path,include
from.views import gatos,index,perros,patan,coraje,scooby,tom,doraemon,garfield

urlpatterns=[
    path('',index,name='INDEX'),
    path('gatos/',gatos,name='GA'),
    path('perros/',perros,name='PE'),
    path('coraje/',coraje,name='COR'),
    path('doraemon/',doraemon,name='DOR'),
    path('garfield/',garfield,name='GAR'),
    path('patan/',patan,name='PAT'),
    path('scooby/',scooby,name='SCO'),
    path('tom/',tom,name='TOM'),
]