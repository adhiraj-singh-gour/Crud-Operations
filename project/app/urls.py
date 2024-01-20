from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('insert',insert,name='insert'),
    path('show/',show,name='show'),
    
    path('editpage/<int:pk>/',editpage,name='editpage'),
    path('edit/<int:pk>/',edit,name='edit'),
    path('deletepage/<int:pk>/',deletepage,name='deletepage'),
]
