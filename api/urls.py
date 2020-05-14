
from django.urls import path,include
from . import views

urlpatterns = [
    path("article/",views.ArticleAPIView.as_view()), 
    path('detail/<int:id>',views.ArticleDetails.as_view()),
    path('generic/article/<int:id>',views.GenericAPIView.as_view()),
]
