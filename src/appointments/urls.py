from django.urls import path

from . import views
app_name = 'appointments'


urlpatterns = [
    path('add-appointment/', views.add_appointment, name='add-appointment'),
    path('submit-appointment/', views.submit_appointment, name='submit-appointment'),
    path('delete-appointment/<int:id>', views.delete_appointment, name='delete-appointment'),
    path('list-appointment', views.list_appointment, name='list-appointment'),
    path('edit-appointment/<int:id>', views.edit_appointment, name='edit-appointment'),
    path('update-appointment/<int:id>', views.update_appointment, name='update-appointment')

]