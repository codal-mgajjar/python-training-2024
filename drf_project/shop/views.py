from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer

# Class based view
class ItemListView(APIView):
    def get(self, request, *args, **kwargs):
        items = Item.objects.all()
    
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#function based view
@api_view()
def hello_world(request):
    return Response({"message": "Hello world"})

#Api policy decorator
from rest_framework.decorators import throttle_classes
from rest_framework.throttling import UserRateThrottle

class OncePerDayUserThrottle(UserRateThrottle):
    rate = '1/day'

@api_view(['GET'])
@throttle_classes([OncePerDayUserThrottle])
def view(request):
    return Response({"message": "Hello for today! See you tomorrow!"})


#View schema decorator
from rest_framework.decorators import schema
from rest_framework.schemas import AutoSchema

class CustomAutoSchema(AutoSchema):
    def get_link(self, path, method, base_url):
        # override view introspection here...
        def view_schema_decorator():
            return Response({"message": "Hello for today!"})
            

@api_view(['GET'])
@schema(CustomAutoSchema())
def view_schema_decorator(request):
    return Response({"message": "Hello for today! See you tomorrow!"})

#Genericview
from django.contrib.auth.models import User
from shop.serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
    
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from shop.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response

#viewset example
# class UserViewSet(viewsets.ViewSet):
#     """
#     A simple ViewSet for listing or retrieving users.
#     """
#     def list(self, request):
#         queryset = User.objects.all()
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = User.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = UserSerializer(user)
#         return Response(serializer.data)

#ModelViewset example
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


#For routing
from rest_framework.decorators import action

class ItemsViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer

    def get_queryset(self):
        items = Item.objects.all()
        return items
    

    #Routing for extra actions
    @action(methods=['post'], detail=True, url_path='change-price', url_name='change_price')
    def set_price(self, request, pk=None):
        item = self.get_object()  
        new_price = request.data.get('price')
        item.price = new_price
        item.save()
        return Response({'message': 'Price updated successfully', 'new_price': new_price})

from rest_framework.parsers import JSONParser, FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

class ExampleView(APIView):
    parser_classes = [JSONParser]

    def post(self, request, format=None):
        return Response({'received data': request.data})
    
class FileUploadView(APIView):
    parser_classes = [FileUploadParser]

    def put(self, request, filename, format=None):
        file_obj = request.data['file']
        # ...
        # do some stuff with uploaded file
        # ...
        return Response(status=204)

from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

class UserCountView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        user_count = User.objects.filter().count()
        content = {'user_count': user_count}
        return Response(content)