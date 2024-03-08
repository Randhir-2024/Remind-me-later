from django.shortcuts import render, redirect
from .forms import ReminderForm

def create_reminder(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')  # Redirect to a success page or any other URL
    else:
        form = ReminderForm()
    return render(request, 'create_reminder.html', {'form': form})
