from django.urls import path
from . import views

app_name = 'App_Folder'

urlpatterns = [
    path('index/',views.index_view,name='index'),
    path('relative/',views.relative_view,name='relative'),
    path('other/',views.other_view,name='other'),
]
