from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from tracker.models import PleasantHabit, UsefulHabit
from tracker.paginators import HabitPagination
from tracker.serializers import PleasantHabitSerializer, UsefulHabitSerializer
from users.permissions import IsOwner


class PleasantHabitViewSet(viewsets.ModelViewSet):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all()
    pagination_class = HabitPagination

    def perform_create(self, serializer):
        pleasant_habit = serializer.save(user=self.request.user)
        pleasant_habit.save()

    def get_queryset(self):
        user = self.request.user
        return PleasantHabit.objects.filter(user=user)

    def get_permissions(self):
        if self.action in ("list", "update", "destroy", "retrieve"):
            self.permission_classes = (IsAuthenticated, IsOwner)
        return super().get_permissions()


class UsefulHabitCreateView(generics.CreateAPIView):
    serializer_class = UsefulHabitSerializer

    def perform_create(self, serializer):
        useful_habit = serializer.save(user=self.request.user)
        useful_habit.save()


class PublishedUsefulHabitListView(generics.ListAPIView):
    queryset = UsefulHabit.objects.filter(is_published=True)
    serializer_class = UsefulHabitSerializer
    pagination_class = HabitPagination


class UsefulHabitListView(generics.ListAPIView):
    serializer_class = UsefulHabitSerializer
    pagination_class = HabitPagination
    permission_classes = (IsAuthenticated, IsOwner)

    def get_queryset(self):
        user = self.request.user
        return UsefulHabit.objects.filter(user=user)


class UsefulHabitDetailView(generics.RetrieveAPIView):
    queryset = UsefulHabit.objects.all()
    serializer_class = UsefulHabitSerializer
    permission_classes = (IsAuthenticated, IsOwner)


class UsefulHabitUpdateView(generics.UpdateAPIView):
    queryset = UsefulHabit.objects.all()
    serializer_class = UsefulHabitSerializer
    permission_classes = (IsAuthenticated, IsOwner)


class UsefulHabitDeleteView(generics.DestroyAPIView):
    queryset = UsefulHabit.objects.all()
    serializer_class = UsefulHabitSerializer
    permission_classes = (IsAuthenticated, IsOwner)
