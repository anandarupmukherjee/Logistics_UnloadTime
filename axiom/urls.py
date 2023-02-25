
from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path("home/", views.home, name="home"),
    path("update/", views.update, name="update"),
    path("createpost/", views.createpost, name="createpost"),
    path('analysis/', views.analysis, name='analysis'),
    path('analysis1/', views.analysis1, name='analysis1'),
    path('analysis2/', views.analysis2, name='analysis2'),
    path('export/', views.csv_database_write, name='csv_database_write'),
    path('summary/', views.summary, name='summary'),
    path('admin/', views.admin, name='admin'),
#    path("insights/", views.insights, name="insights")

]
