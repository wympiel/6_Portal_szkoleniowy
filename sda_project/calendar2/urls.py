from django.conf.urls import url
from . import views

app_name = 'calendar2'
urlpatterns = [

    url(r'^$', views.CalendarView.as_view(), name='calendar2'),
]
