from rest_framework import viewsets, generics

# Create your views here.
from tracker.models import PleasantHabit, UsefulHabit
from tracker.serializers import PleasantHabitSerializer, UsefulHabitSerializer


class PleasantHabitViewSet(viewsets.ModelViewSet):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all()

    def perform_create(self, serializer):
        pleasant_habit = serializer.save(user=self.request.user)
        pleasant_habit.save()


class UsefulHabitCreateView(generics.CreateAPIView):
    serializer_class = UsefulHabitSerializer

    def perform_create(self, serializer):
        useful_habit = serializer.save(user=self.request.user)
        useful_habit.save()


class UsefulHabitListView(generics.ListAPIView):
    queryset = UsefulHabit.objects.all()
    serializer_class = UsefulHabitSerializer


class UsefulHabitDetailView(generics.RetrieveAPIView):
    queryset = UsefulHabit.objects.all()
    serializer_class = UsefulHabitSerializer


class UsefulHabitUpdateView(generics.UpdateAPIView):
    queryset = UsefulHabit.objects.all()
    serializer_class = UsefulHabitSerializer


class UsefulHabitDeleteView(generics.DestroyAPIView):
    queryset = UsefulHabit.objects.all()
    serializer_class = UsefulHabitSerializer
