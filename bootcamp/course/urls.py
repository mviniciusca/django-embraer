from django.urls import path
from .views import courseindex, coursecreate, courseedit

urlpatterns = [
    path('', courseindex, name='courseIndex'),
    path('create', coursecreate, name="couseCreate"),
    path('edit/<int:user_id>', courseedit, name="courseEdit")
]