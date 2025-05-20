from django.contrib import admin
from .models import TrackSoldier, RequestCall, FlightBooking, MedicalReport,LeavePassRequest

admin.site.register(TrackSoldier)
admin.site.register(RequestCall)
admin.site.register(FlightBooking)
admin.site.register(MedicalReport)
admin.site.register(LeavePassRequest)
