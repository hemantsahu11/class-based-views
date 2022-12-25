from django.urls import path
from . import views

app_name = 'classroom'     # the app name will come handy in calling view from templates like   appname: thankyou  (like reverse )

urlpatterns =[
    path('', views.HomeView.as_view(), name='home'),    # path expects  a function
    path('thankyou/', views.ThankYouView.as_view(), name='thankyou'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('create_teacher/', views.TeacherCreateView.as_view(), name='create_teacher'),
    path('teacher_list', views.TeacherListView.as_view(), name='teacher_list'),
    path('teacher_detail/<int:pk>/', views.TeacherDetailView.as_view(), name='teacher_detail'),
    path('update_teacher/<int:pk>/', views.TeacherUpdateView.as_view(), name='update_teacher'),
    path('delete_teacher/<int:pk>/', views.TeacherDeleteView.as_view(), name='delete_teacher'),
]