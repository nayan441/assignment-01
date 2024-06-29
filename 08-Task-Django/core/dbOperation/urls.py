# myapp/urls.py
from django.urls import path
from .views import upload_data, get_latest_records

urlpatterns = [
    path('upload/', upload_data, name='upload_data'),
    path('latest-records/', get_latest_records, name='get_latest_records'),

]