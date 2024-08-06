from rest_framework import generics
from .models import Reservation
from .serializers import ReservationSerializer
from rest_framework.permissions import IsAuthenticated

class ReservationListCreateView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)