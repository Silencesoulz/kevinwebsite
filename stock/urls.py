from django.urls import path
from . import views

urlpatterns =[
  path('',views.index, name='index'),
  path('about',views.about, name='about'),
  path('contact',views.contact, name='contact'),
  path('reference',views.reference, name='reference'),
  path('toeic',views.toeic, name='toeic'),
  path('cert',views.cert, name='cert'),
]
