from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login,logout
from django.views.generic import *
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import *
from django.contrib import messages
from . forms import *

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



@method_decorator(login_required, name='dispatch')
class SoldierListView(ListView):
    model = TrackSoldier
    template_name = 'usdefencsupport/soldier_list.html'
    context_object_name = 'soldiers'


@method_decorator(login_required, name='dispatch')
class SoldierCreateView(CreateView):
    model = TrackSoldier
    fields = '__all__'
    template_name = 'usdefencsupport/soldier_form.html'
    success_url = reverse_lazy('soldier_list')

@method_decorator(login_required, name='dispatch')
class SoldierUpdateView(UpdateView):
    model = TrackSoldier
    fields = '__all__'
    template_name = 'usdefencsupport/soldier_form.html'
    success_url = reverse_lazy('soldier_list')

@method_decorator(login_required, name='dispatch')
class SoldierDeleteView(DeleteView):
    model = TrackSoldier
    template_name = 'usdefencsupport/soldier_confirm_delete.html'
    success_url = reverse_lazy('soldier_list')


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





@method_decorator(login_required, name='dispatch')
def leavepass_list(request):
    leavepasses = LeavePassRequest.objects.all()
    return render(request, 'leavepass/leavepass_list.html', {'leavepasses': leavepasses})

# Create new leave pass request
def leavepass_create(request):
    if request.method == 'POST':
        form = LeavePassRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leavepass_list')
    else:
        form = LeavePassRequestForm()
    return render(request, 'leavepass/leavepass_form.html', {'form': form, 'title': 'Add Leave Pass'})

@method_decorator(login_required, name='dispatch')
def leavepass_edit(request, pk):
    leavepass = get_object_or_404(LeavePassRequest, pk=pk)
    if request.method == 'POST':
        form = LeavePassRequestForm(request.POST, instance=leavepass)
        if form.is_valid():
            form.save()
            return redirect('leavepass_list')
    else:
        form = LeavePassRequestForm(instance=leavepass)
    return render(request, 'leavepass/leavepass_form.html', {'form': form, 'title': 'Edit Leave Pass'})

@method_decorator(login_required, name='dispatch')
def leavepass_delete(request, pk):
    leavepass = get_object_or_404(LeavePassRequest, pk=pk)
    if request.method == 'POST':
        leavepass.delete()
        return redirect('leavepass_list')
    return render(request, 'leavepass/leavepass_confirm_delete.html', {'leavepass': leavepass})







@method_decorator(login_required, name='dispatch')
class RequestCallListView(ListView):
    model = RequestCall
    template_name = 'usdefencsupport/request_call_list.html'
    context_object_name = 'requests'

@method_decorator(login_required, name='dispatch')
class FlightBookingListView(ListView):
    model = FlightBooking
    template_name = 'usdefencsupport/flight_booking_list.html'
    context_object_name = 'flights'

@method_decorator(login_required, name='dispatch')
class MedicalReportListView(ListView):
    model = MedicalReport
    template_name = 'usdefencsupport/medical_report_list.html'
    context_object_name = 'reports'



def admin_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('admin_dashboard')  # You will create this page next
        else:
            messages.error(request, 'Invalid credentials or not authorized.')

    return render(request, 'usdefencsupport/admin_login.html')


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('home')  # Redirect to your home


@login_required
def admin_dashboard_view(request):
    if not request.user.is_staff:
        messages.error(request, 'You are not authorized to access this page.')
        return redirect('admin_login')

    return render(request, 'usdefencsupport/admin_dashboard.html')