import uuid
from .misc import without_keys
from rest_framework import status
from rest_framework import generics
from django.contrib.auth import login
from  .FilterSet import PropertyFilter
from rest_framework.response import Response
from rest_framework import permissions
from .models import Property,Location,Images 
from .serializers import PropertySerializer,LocationSerializer,ImagesSerializer,LoginSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView


class PropertyList(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    filterset_class = PropertyFilter
    permission_classes = [permissions.AllowAny]
        

class PropertyDetail(generics.RetrieveAPIView):
    serializer_class = PropertySerializer
    queryset = Property.objects.all()
    lookup_field = 'property_id'
    permission_classes = [permissions.AllowAny]


class AddProperty(generics.CreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAdminUser]

    def post(self, request, *args, **kwargs):
        success = False
        previews_data = {}
        response = {'Success':success}
        form_images = {'_'.join(k.lower().split(' ')): v for k, v in request.FILES.items()}
        request_data = {'_'.join(k.lower().split(' ')): v for k, v in request.data.items()}
        
        preview_images = without_keys(form_images,{'property_image',})

        serializer = PropertySerializer(data=request_data)
        if serializer.is_valid():
            property = serializer.save()

            previews_data['property'] = uuid.UUID(str(property))

            for images in preview_images.values():
                previews_data['images']=images
                Imgserializer = ImagesSerializer(data=previews_data)
                if Imgserializer.is_valid():
                    Imgserializer.save()
                    success = True
                else:
                    success = False            
        else:
            success = False
            response['Success'] = success
            
            print(serializer.errors,'JUYHIUHGJUIHJGJUIHUIHGUJGHJUG')
            # print(serializer.errors['title'][0],'OIUHJKIOUHG')

        if success:
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            return Response(response,status=status.HTTP_400_BAD_REQUEST)
        
    

class LocationList(generics.ListCreateAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    permission_classes = [permissions.AllowAny]


class LocationDetail(generics.RetrieveAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    permission_classes = [permissions.AllowAny]


class ImagesList(generics.ListAPIView):
    serializer_class = ImagesSerializer
    queryset = Images.objects.all()
    filterset_fields = ['property']
    permission_classes = [permissions.AllowAny]


class UploadImageView(generics.ListCreateAPIView):
    serializer_class = ImagesSerializer
    queryset = Images.objects.all()
    permission_classes = [permissions.AllowAny]
