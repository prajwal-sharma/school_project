from django.conf.urls import url
from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [

    path("", views.SchoolListView.as_view(), name='list'),
    path('<int:pk>/', views.SchoolDetailView.as_view(), name='detail'),
    path("create/", views.SchoolCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.SchoolUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.SchoolDeleteView.as_view(), name='delete'),
    path("student/", views.StudentListView.as_view(), name='studentlist'),
    path('student/<int:pk>/', views.StudentDetailView.as_view(), name='studentdetail'),
    path("create_student/", views.StudentCreateView.as_view(), name='createstudent'),
    path('delete_student/<int:pk>/', views.StudentDeleteView.as_view(), name='deletestudent'),
]
