from django.urls import path
from.import views

urlpatterns = [
    path('first', views.new,name="first"),
    path('second', views.new1,name="second"),
    path('third', views.new2,name="third"),
    path('fourth', views.new3,name="fourth"),
    path('fifth', views.new4,name="fifth")

]