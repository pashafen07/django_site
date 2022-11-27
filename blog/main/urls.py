from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('blog/', blog, name='blog'),
    path('new-blog/', new_blog, name='new_blog')
]
