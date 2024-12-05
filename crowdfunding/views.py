from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.permissions import IsAdminOrCreator, IsDonor
from .models import Project, Donation
from .serializers import ProjectSerializer, DonationSerializer


class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_permissions(self):
        
        if self.request.method == 'POST':
            return [IsAdminOrCreator()]
        
        return [AllowAny()]

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class DonationList(generics.ListCreateAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    permission_classes = [IsDonor]


