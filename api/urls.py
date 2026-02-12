from django.urls import path
from api import views

app_name = 'api'

urlpatterns = [
    path('schedules/<int:id>/',views.get_shedule),
    path('schedule/create/',views.create_shedule),
    path('schedule/<int:id>/update/',views.update_shedule),
    path('schedule/<int:id>/delete/',views.delete_shedule),

]