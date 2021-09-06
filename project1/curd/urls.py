from django.urls import path
from curd import views
urlpatterns= [
    path(r'curdlist/',views.curd_list,name="curd_list"),
    path(r'curddetail/<pk>/',views.curd_detail,name="curd_detail"),
    path(r'curd/<name>/',views.curd,name="curd"),
    #path(r'sample/',views.sample,name="sample"),
]