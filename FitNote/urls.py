from django.urls import path
from .views import WorkoutListView, WorkoutDetailView, ExerciseUpdateView, WorkoutCreateView, WorkoutDeleteView, ExerciseDeleteView, WorkoutNoteCreateFormView

urlpatterns = [
    path('', WorkoutListView.as_view(), name='workout_list'),
    path('<int:pk>/', WorkoutDetailView.as_view(), name='workout_detail'),
    path('new/', WorkoutCreateView.as_view(), name='workout_create'),
    path('<int:pk>/edit/', ExerciseUpdateView.as_view(), name='exercise_update'),
    path('<int:pk>/addexercise/', WorkoutNoteCreateFormView, name='exercise_create'),
    path('<int:pk>/deleteexercise/', ExerciseDeleteView.as_view(), name='exercise_delete'),
    path('<int:pk>/deleteworkout/', WorkoutDeleteView.as_view(), name='workout_delete')
]