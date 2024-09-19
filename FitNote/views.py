from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Note, Workout, Exercise
from .forms import WorkoutNoteCreateForm


class WorkoutListView(ListView):
    model = Workout
    template_name = "workout_list.html"
    context_object_name = "workouts"


class WorkoutCreateView(CreateView):
    model = Workout
    template_name = "workout_create.html"
    fields = ['title', 'date']
    context_object_name = "note"
    success_url = reverse_lazy('workout_list')


class WorkoutDetailView(DetailView):
    model = Workout
    template_name = "workout_detail.html"
    
    def get(self, request, *args, **kwargs):
        #get everything about this workout - title, exercises/sets/reps/weight from joint table (notes),
        workout_title = Workout.objects.filter(id=kwargs['pk'])[0]
        notes = Note.objects.values().filter(workout_id=kwargs['pk'])
        note_ids = [notes[i]["id"] for i in range(len(notes))]
        exercise = [Exercise.objects.filter(id=notes[i]["exercise_id_id"])[0] for i in range(len(notes))]
        sets = [notes[i]["sets"] for i in range(len(notes))]
        reps = [notes[i]["reps"] for i in range(len(notes))]
        weight = [notes[i]["weight"] for i in range(len(notes))]
        context = {
            'exercises': zip(note_ids,exercise,sets,reps,weight), 
            'workout_id': kwargs['pk'], 
            'workout_title': workout_title
        }
        return render(request, self.template_name, context)


class ExerciseUpdateView(UpdateView):
    model = Note
    template_name = "exercise_update.html"
    fields = ['exercise_id', 'reps', 'sets', 'weight']

    def get_success_url(self):
        workout_id = Note.objects.values_list().filter(pk = self.kwargs['pk'])[0][1]
        return reverse_lazy('workout_detail', kwargs={'pk': workout_id})


class WorkoutDeleteView(DeleteView):
    model = Workout
    template_name = "workout_delete.html"
    success_url = reverse_lazy('workout_list')


class ExerciseDeleteView(DeleteView):
    model = Note
    template_name = "exercise_delete.html"

    def get_success_url(self):
        workout_id = Note.objects.values_list().filter(pk = self.kwargs['pk'])[0][1]
        return reverse_lazy('workout_detail', kwargs={'pk': workout_id})


def WorkoutNoteCreateFormView(request, pk):

    #get all exercises and its ids
    exercises = [(id, exer) for id, exer in list(Exercise.objects.values_list())]

    if request.method == "POST":
        form = WorkoutNoteCreateForm(request.POST)
        updated_data = request.POST.copy()
        #adds workout id to the form
        updated_data.update({'workout_id': pk})
        form = WorkoutNoteCreateForm(data=updated_data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('workout_detail', kwargs={'pk': pk}))
    else:
        form = WorkoutNoteCreateForm()

    return render(request, 'workout_exericse_create.html', {'form': form, 'exercises': exercises})