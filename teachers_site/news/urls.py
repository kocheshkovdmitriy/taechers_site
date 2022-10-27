from django.urls import path
from .views import  *


urlpatterns = [
    path('', new_list, name='news'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('news/create_new/', NewFormView.as_view(), name='create_new'),
    path('news/<int:pk>/edit/', NewEditView.as_view(), name='edit_new'),
    path('news/<int:pk>/create_commit/', CommitFormView.as_view(), name='create_commit'),
]