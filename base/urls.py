from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #  path('login/', views.loginPage, name="login"),
    # path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name="home"),
    path('events/',views.events, name="events"),
    path('dashboard/',views.events, name="dashboard"),
    path('create-event/',views.createEvent, name="create-event"),
    path('event/<str:pk>',views.singlEvent, name="event"),
    path('update-event/<str:pk>/',views.updateEvent, name="update-event"),


    # path('room_page/<str:pk>/', views.room, name="room"),

    # path('create-room/', views.createRoom, name="create-room"),
    #  path('update-room/<str:pk>', views.updateRoom, name="update-room"),
    #  path('delete-room/<str:pk>', views.deleteRoom, name="delete-room"),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
