from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event, Registration
from .forms import EventForm
from django.views.generic import ListView

class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    ordering = ['date']

def event_list(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    already_registered = False
    if request.user.is_authenticated:
        already_registered = Registration.objects.filter(event=event, attendee=request.user).exists()
    return render(request, 'events/event_detail.html', {'event': event, 'already_registered': already_registered})

@login_required
def event_create(request):
    if request.user.role != 'organizer':
        messages.error(request, 'Solo gli organizer possono creare eventi.')
        return redirect('events:list')
    form = EventForm(request.POST or None)
    if form.is_valid():
        event = form.save(commit=False)
        event.organizer = request.user
        event.save()
        messages.success(request, 'Evento creato con successo!')
        return redirect('events:detail', pk=event.pk)
    return render(request, 'events/event_form.html', {'form': form})

@login_required
def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.user != event.organizer:
        messages.error(request, 'Non puoi modificare questo evento.')
        return redirect('events:detail', pk=pk)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        messages.success(request, 'Evento modificato con successo!')
        return redirect('events:detail', pk=event.pk)
    return render(request, 'events/event_form.html', {'form': form})

@login_required
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.user != event.organizer:
        messages.error(request, 'Non puoi eliminare questo evento.')
        return redirect('events:detail', pk=pk)
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Evento eliminato.')
        return redirect('events:list')
    return render(request, 'events/event_confirm_delete.html', {'event': event})

@login_required
def event_register(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.user.role != 'attendee':
        messages.error(request, 'Solo gli attendee possono registrarsi agli eventi.')
        return redirect('events:detail', pk=pk)
    Registration.objects.get_or_create(event=event, attendee=request.user)
    messages.success(request, 'Registrazione effettuata!')
    return redirect('events:detail', pk=pk)

@login_required
def event_unregister(request, pk):
    event = get_object_or_404(Event, pk=pk)
    Registration.objects.filter(event=event, attendee=request.user).delete()
    messages.success(request, 'Registrazione annullata.')
    return redirect('events:detail', pk=pk)