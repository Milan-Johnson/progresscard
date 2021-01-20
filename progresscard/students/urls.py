from django.urls import path
from . import views

urlpatterns = [
    path('postmarks',views.postmarks,name='postmarks'),
]   