from django.urls import path
from . import views


app_name = 'booth'
urlpatterns = [
    # path('make_booth/', views.make_booth, name='make_booth'), csv 파일 DB에 등록할 때만 사용하는 URL.
    path('', views.maps, name='index'),
]
