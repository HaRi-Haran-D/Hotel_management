# import datetime
# from myapp.models import Room, Booking

# def check_availability(room,check_in,check_out):
#     avail_list=[]
#     booking_list=Booking.objects.filter(room=room)
#     for booking in booking_list:
#         if booking.check_in > check_out or booking.check_out < check_in:
#             avail_list.append(True)
#         else:
#             avail_list.append(False)
#     return all(avail_list)

from datetime import datetime
from myapp.models import Booking

def check_availability(room, check_in, check_out):
    # Normalize inputs to date objects (Booking uses DateField)
    if isinstance(check_in, datetime):
        check_in = check_in.date()
    if isinstance(check_out, datetime):
        check_out = check_out.date()

    booking_list = Booking.objects.filter(room=room)
    for booking in booking_list:
        # if bookings overlap, room is not available
        if not (booking.check_in > check_out or booking.check_out < check_in):
            return False
    return True
