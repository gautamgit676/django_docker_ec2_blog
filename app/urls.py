from django.urls import path
from app.views import home,StudentView


urlpatterns = [
  path('home/',home, name='home'),
  path('stu/',StudentView, name='stu' )
]
