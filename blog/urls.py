from django.urls import path
from .views import ArticleListView,CategorieListView,ArticleDetailView,Inscription,updateCommente,commentDelete

urlpatterns = [
    path('',ArticleListView.as_view(),name='Liste_article'),
    path('categorie/',CategorieListView.as_view(),name='Liste_categorie'),
    path('<int:pk>',ArticleDetailView.as_view(),name='detail_article'),
    path('<int:pk>/edit/',updateCommente.as_view(),name='update'),
    path('<int:pk>/delet/',commentDelete.as_view(),name='delet'),
    path('register/', Inscription.as_view(),name='inscription')
]
