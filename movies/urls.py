from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='movies.index'),
    path('<int:id>/', views.show, name='movies.show'),
    path('<int:id>/review/create/', views.createReview, name='movies.create_review'),
    path('<int:id>/review/<int:review_id>/edit/', views.editReview, name='movies.edit_review'),
    path('<int:id>/review/<int:review_id>/delete/', views.deleteReview, name='movies.delete_review'),
]