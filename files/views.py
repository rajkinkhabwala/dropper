from rest_framework import status, viewsets, parsers, permissions
from rest_framework.response import Response
from .models import Upload
from .serializers import FileSerializer

class FileViewSet(viewsets.ModelViewSet):
    permission_classes  = [permissions.AllowAny]
    serializer_class = FileSerializer
    queryset= Upload.objects.all()
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

    # def create(self, request, format=None):
    #     print("hello from create")
    #     print(request.data)
    #     serializer = FileSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    # def get_queryset(self):
    #         user = self.request.user
    #         return Upload.objects.filter(user=user)