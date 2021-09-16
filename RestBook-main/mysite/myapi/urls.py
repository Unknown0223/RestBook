from django.urls import path, include
from rest_framework import routers
from .views import *

# router = routers.DefaultRouter()
# router.register(r"authors", AuthorViewSet)
# router.register(r"categories", CategoryViewSet)
# router.register(r"books", BookViewSet)
urlpatterns = [
    # path('', include(router.urls)),


    # path('authors/', AuthorView.as_view(), name='authors-list'),
    # path('authors/<int:pk>/', AuthorView.as_view(), name='authors-list'),
    #
    # path('categories/', CategoryView.as_view(), name='categories-list'),
    # path('categories/<int:pk>/', CategoryView.as_view(), name='categories-list'),
    #
    # path('books/', BookView.as_view(), name='books-list'),
    # path('books/<int:pk>/', BookView.as_view(), name='books-list'),

    ##################################################################

    path('authors/create/', AuthorCreateView.as_view(), name="author-create"),

    path('authors/list/', AuthorView.as_view(), name="author-list"),

    path('authors/<int:pk>/retrieve/', AuthorRetrieveView.as_view(), name="author-retrieve"),
    path('authors/<int:pk>/update/', AuthorUpdateView.as_view(), name="author-update"),
    path('authors/<int:pk>/destroy/', AuthorDestroyView.as_view(), name="author-destroy"),

    path('categories/create/', CategoryCreateView.as_view(), name="category-create"),
    path('categories/list/', CategoryListView.as_view(), name="author-list"),
    path('categories/<int:pk>/retrieve/', CategoryRetrieveView.as_view(), name="category-retrieve"),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name="category-update"),
    path('categories/<int:pk>/destroy/', CategoryDestroyView.as_view(), name="category-destroy"),

    path('books/create/', BookCreateView.as_view(), name="book-create"),
    path('books/list/', BookView.as_view(), name="book-list"),
    path('books/<int:pk>/retrieve/', BookView.as_view(), name="book-retrieve"),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name="book-update"),
    path('books/<int:pk>/destroy/', BookDestroyView.as_view(), name="book-destroy"),

]