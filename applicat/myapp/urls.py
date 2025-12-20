from django.urls import path
from myapp.views import RoomList, BookingList, BookingView
app_name = 'myapp'
#from myapp import views

urlpatterns = [
    path('booking_list/', BookingList.as_view(),name = 'Booking_list'),
    path('room_list/', RoomList.as_view(),name = 'Room_list'),
    path('book/', BookingView.as_view(), name='book' ),
]
