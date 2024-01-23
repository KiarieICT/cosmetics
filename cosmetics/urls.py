from . import views
from django.urls import path

app_name="cosmetics"
urlpatterns=[
           path("",views.first, name="first"),  
]