from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # All posts
    path('posts/', views.posts, name='posts'),

    # Categories
    path('categories/', views.categories, name='categories'),

    # ta jedna cateogira
    path('categories/<int:catego_id>/', views.catego, name='catego'),

    # post jeden
    path('posts/<int:post_id>/', views.post, name='post'),

    # ex: /xd/
    path('xd', views.IndexView.as_view(), name='index2'),
    # ex: /xd/5/
    path('xd/<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /xd/5/results/
    path('xd/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /xd/5/vote/
    path('xd/<int:question_id>/vote/', views.vote, name='vote'),

    # page for adding new category
    path('new_catego/', views.new_catego, name='new_catego'),

    #new post
    path('new_post/<int:catego_id>/', views.new_post, name='new_post'),

    path('name', views.get_name, name='name')
]