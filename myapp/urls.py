from django.urls import path
from .views import (
    home,
    save_data,
    delete_record,
    edit_record,
    )

urlpatterns = [
    path('',home, name='home'),
    path('save/',save_data,name='save'),
    path('delete_record/',delete_record,name='delete_record'),
    path('edit/',edit_record,name='edit'),

]
