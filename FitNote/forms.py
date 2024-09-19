from django import forms
from .models import Note, Exercise

class WorkoutNoteCreateForm(forms.Form):
    workout_id = forms.IntegerField(required=True, widget=forms.HiddenInput())
    exercise_id = forms.ModelChoiceField(required=True, queryset=Exercise.objects.values())
    sets = forms.IntegerField(required=True)
    reps = forms.IntegerField(required=True)
    weight = forms.IntegerField(required=True)

    def save(self, commit=True):
        note = Note(workout_id_id = int(self.cleaned_data['workout_id']),
                    exercise_id_id = self.cleaned_data['exercise_id']['id'],
                    sets = int(self.cleaned_data['sets']),
                    reps = int(self.cleaned_data['reps']),
                    weight = int(self.cleaned_data['weight']))
        note.save()
        return note
