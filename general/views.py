from django.shortcuts import render, redirect
from .models import Bin, Teacher, Booked_Bin

# Create your views here.
def home(request):
    all_bins = Bin.objects.all
    print(request.user.username)
    return render(request, 'dupe_home.html',{'all':all_bins})

def login(request):
    return render(request, 'login.html')

"""
def book(request):
    all_bins = Bin.objects.all # DON NOT FOROGET TO PUT IN CURLY BRACKETS
    all_booked = Booked_Bin.objects.all
    return render(request, 'dupe_book.html',{'all_b':all_booked})
"""
def my_bookings(request):
    username = request.user.username
    if username=='admin':
        teacher = Teacher.objects.all
        bookings = Booked_Bin.objects.all().select_related('bin').order_by('-date')
        return render(request, 'my_bookings_dupe.html', {'bookings': bookings,'username':username})
    elif Teacher.objects.filter(username=username).exists():
        teacher = Teacher.objects.get(username=username)
        bookings = Booked_Bin.objects.filter(teacher=teacher).select_related('bin').order_by('-date')
        return render(request, 'my_bookings_dupe.html', {'bookings': bookings, 'username' : username})
    else:
        return render(request, 'illegal.html')

    #user_bins = Booked_Bin.objects.filter(period="1A").select_related('bin','teacher')
    #return render(request, 'display_info.html', {'f_bins': filtered_bins, 'selected_period': "1A"})

def test(request):
    all_bins = Bin.objects.all
    return render(request, 'test.html', {'all':all_bins})

def join(request):
    return render(request, 'join.html', {})

def testing(request):
    filtered_bins = Booked_Bin.objects.filter(date="2023-05-30").values()
    return render(request, 'dupe_book.html',{'filtered_b':filtered_bins})

def select_option(request):
    if request.method == 'POST':
        # retrieve date and period user selects
        selected_date = request.POST.get('Date')
        selected_period = request.POST.get('Period')
        
        # query the database based on the selected period and retrieve the relevant information
        # broken hlep filtered_bins = Booked_Bin.objects.all()
        if selected_date and selected_period:
            # filtered_bins = Booked_Bin.objects.filter(date=selected_date, period=selected_period).select_related('bin')
                # Retrieve all bins that do not have a corresponding row in Booked_Bin for the selected date and period
            #booked_bins = Booked_Bin.objects.filter(date=selected_date, period=selected_period)
            #booked_bins = booked_bins.select_related('bin')
            #available_bins = Bin.objects.exclude(booked_bins)
            available_bins = Bin.objects.exclude(bookings__date=selected_date, bookings__period=selected_period)

            return render(request, 'display_info.html', {'f_bins': available_bins, 'selected_period': selected_period, 'selected_date': selected_date})
    return render(request, 'dupe_book.html')

def verify(request):
    return render(request, 'verify.html')

def book_bin(request):
    if request.method == 'POST':
        bin_id = request.POST.get('bin_id')
        date = request.POST.get('date')
        period = request.POST.get('period')
        username = request.POST.get('username')
        teacher = Teacher.objects.get(username=username)
        teacher_id = teacher.teacher_id
        # Create a new Booked_Bin object with the selected bin and additional information

        booked_bin = Booked_Bin.objects.create(bin_id=bin_id, date=date, period=period, teacher_id=teacher_id)
        # Redirect the user to a success page or another appropriate view
        return redirect(my_bookings)