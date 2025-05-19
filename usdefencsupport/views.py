from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import *
from django.contrib import messages

class HomePageView(TemplateView):
    template_name = 'usdefencsupport/index.html'

class AboutPageView(TemplateView):
    template_name = 'usdefencsupport/about.html'

def request_call_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile_carrier = request.POST.get('mobile_carrier')
        country = request.POST.get('country')
        minute_requested = request.POST.get('minute_requested')
        country_of_deploy = request.POST.get('country_of_deploy')
        name_of_soldier = request.POST.get('name_of_soldier')

        RequestCall.objects.create(
            name=name,
            email=email,
            mobile_carrier=mobile_carrier,
            country=country,
            minute_requested=minute_requested,
            country_of_deploy=country_of_deploy,
            name_of_soldier=name_of_soldier,
        )
        messages.success(request, "Request successfully submitted.")
        return redirect('request_call')
    
    return render(request, 'usdefencsupport/request_call.html')

def track_soldier_view(request):
    soldier = None
    if request.method == 'POST':
        name = request.POST.get('soldier_name')
        try:
            soldier = TrackSoldier.objects.get(name__iexact=name)
        except TrackSoldier.DoesNotExist:
            messages.error(request, 'Soldier not found.')

    return render(request, 'usdefencsupport/track_soldier.html', {'soldier': soldier})


def book_flight_view(request):
    if request.method == 'POST':
        passenger_name = request.POST.get('passenger_name')
        soldier_name = request.POST.get('soldier_name')
        destination = request.POST.get('destination')
        departure_date = request.POST.get('departure_date')
        contact_email = request.POST.get('contact_email')
        passport_number = request.POST.get('passport_number')

        FlightBooking.objects.create(
            passenger_name=passenger_name,
            soldier_name=soldier_name,
            destination=destination,
            departure_date=departure_date,
            contact_email=contact_email,
            passport_number=passport_number
        )
        messages.success(request, "Flight booked successfully!")
        return redirect('book_flight')

    return render(request, 'usdefencsupport/book_flight.html')


def medical_report_view(request):
    if request.method == 'POST':
        soldier_name = request.POST.get('soldier_name')
        reporter_name = request.POST.get('reporter_name')
        email = request.POST.get('email')
        injury_description = request.POST.get('injury_description')
        treatment_given = request.POST.get('treatment_given')
        estimated_bill = request.POST.get('estimated_bill')

        MedicalReport.objects.create(
            soldier_name=soldier_name,
            reporter_name=reporter_name,
            email=email,
            injury_description=injury_description,
            treatment_given=treatment_given,
            estimated_bill=estimated_bill
        )
        messages.success(request, "Medical report submitted.")
        return redirect('medical_report')

    return render(request, 'usdefencsupport/medical_report.html')
