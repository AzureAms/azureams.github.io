from django.urls import path

from . import views

urlpatterns = [
  path('', views.view_article, name='index'),
  path('add/', views.add, name='add'),
  path('add/addrecord/', views.addrecord, name='addrecord'),
  path('delete/<int:order>', views.delete, name='delete'),
  path('update/<int:order>', views.update, name='update'),
  path('update/updaterecord/<int:order>', views.updaterecord, name='updaterecord'),

]