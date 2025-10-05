from django.urls import path
from .views import *
app_name = 'courses'
urlpatterns = [
#path('', my_fbv, name='courses-list'),
path('', CourseView.as_view(template_name= 'contact.html'), name='courses1-list'),
path('<int:id>/', CourseDetailView.as_view(), name='courses-details'),
path('list/', CourseListView.as_view(), name='courses-list'),
path('create/', CourseCreateView.as_view(), name='courses-create'),
path('<int:id>/update/', CourseUpdateView.as_view(), name='courses-update'),
path('<int:id>/delete/', CourseDeleteView.as_view(), name='courses-delete'),
]