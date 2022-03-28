from django.urls import path
from .views import *

app_name = 'students'

urlpatterns = [
	path('', StudentListView.as_view(), name='list_students'),

	path('student/list/', StudentListView.as_view(), name='list_students'),
	path('student/create/', StudentCreateView.as_view(), name='create_student'),
	path('student/<pk>/edit/', StudentUpdateView.as_view(), name='update_student'),
	path('student/<pk>/detail/', StudentDetailView.as_view(), name='student_detail'),
	path('student/<pk>/delete/', StudentDeleteView.as_view(), name='delete_student'),
]