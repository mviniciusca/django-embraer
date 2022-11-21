from django.urls import path
from .views import courseindex, coursecreate

urlpatterns = [
    path('', courseindex, name='courseIndex'),
    path('create', coursecreate, name="couseCreate")
]