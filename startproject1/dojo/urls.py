from django.urls import path
from . import views

urlpatterns = {
    path('sum/<int:x>/', views.mysum),
}