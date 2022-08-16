from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from . import models

urlpatterns = [
    path('myapi/', views.ContactList.as_view()),
    path('myapi/<int:pk>/', views.ContactDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

