from django.urls import path
from wnvis import views

urlpatterns = [
    path('wnvis',views.input_form),
    path('draw',views.draw)
]
