
from django.urls import path
from . import views

# Create URL patterns here.
app_name = 'papers'     
urlpatterns = [
      path('', views.index, name='index'),
      path('read/<int:paper_id>/', views.read_paper, name='read_paper'),
      path('examination-levels/', views.examination_levels, name='examination_levels'),
      path('subjects/', views.subjects, name='subjects'),
      path('paper-stats/', views.paper_stats, name='paper_stats'),
      
]