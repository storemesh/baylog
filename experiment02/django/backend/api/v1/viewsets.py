from rest_framework import viewsets, status
from rest_framework.response import Response
from profile_data.models import Profile
from .serializers import ProfileSerializer
import time


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ErrorViewset(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        df = pd.DataFrame([10, 20, 30, 40], columns=['c1','c2','c3','c4'])
        return Response({"message":"There are error in this endpoint"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TimeoutViewset(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        time.sleep(70)
        return Response({"message":"everything is fine"}, status=status.HTTP_200_OK)
        # return Response(
        #   {"message":"There are timeout in this endpoint"}
        # , status=status.HTTP_408_REQUEST_TIMEOUT
        # )

        