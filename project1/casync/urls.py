from django.urls import path
from casync import views
urlpatterns=[
   # path('api/',views.api,name="api"),
    path('sapi/',views.async_view),
]