from django.urls import path
from ThesisApp import views

urlpatterns = [
    path('', views.index),
    path('<int:person_id>/', views.update_status),
    path('about',views.about),
    path('form',views.form),
    path('member',views.member),
    path('edit/<person_id>',views.edit),
    path('delete/<person_id>',views.delete),

]