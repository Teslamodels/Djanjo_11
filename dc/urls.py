from django.urls import path
from .views import Mark, Zucerberg

urlpatterns = [
    path('', Mark.as_view(), name='mark'),
    path('story/', Zucerberg.as_view(), name='zuck'),
]