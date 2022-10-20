from functools import partial
from urllib import request, response
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated  #for APIView
from rest_framework import status, viewsets
from rest_framework.decorators import action

# Create your views here.


## Decorators are used to modify fucntion

@api_view(['GET','POST'])     ##api_view is a decorator which is convert existing function into API
def home(request):
    if request.method == 'GET':
        return Response({
            'status': 200,
            "msg": "Yes, Django Rest Framework is working...", 
            "method called ": "GET method is called"
        })
    elif request.method == 'POST':
        return Response({
            'status': 200,
            "msg": "Yes, Django Rest Framework is working...", 
            "method called ": "POST method is called"
        })

@api_view(['GET'])
def get_todo(request):
    todo_objs = Todo.objects.all()
    serializer = TodoSerializer(todo_objs, many = True)
    return Response({
            'status' : True,
            'msg' : 'Todo fetched', 
            'data' : serializer.data
        })

@api_view(['POST'])
def post_todo(request):
    try:
        data = request.data
        serializer = TodoSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            # print(serializer.data)
            return Response({
            'status' : True,
            'msg' : 'success data', 
            'data' : serializer.data
        })
        else:
            return Response({
                'status' : False,
                'msg' : 'invalid data', 
                'data' : serializer.errors
            })

    except Exception as e:
        print(e)
    return Response({
            'status': False,
            'msg': 'Somthing Went Wrong', 
        })

@api_view(['PATCH'])
def patch_todo(request):
    try:
        data = request.data
        if not data.get('uid'):
           return Response({
            'status' : False,
            'msg' : 'uid is required', 
            'data' : {}
        }) 

        obj = Todo.objects.get(uid= data.get('uid'))
        serializer = TodoSerializer(obj, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({
            'status' : True,
            'msg' : 'success data', 
            'data' : serializer.data
        })
        else:
            return Response({
                'status' : False,
                'msg' : 'invalid data', 
                'data' : serializer.errors
            })
    except Exception as e:
        print(e)
        return Response({
            'status': False,
            'msg': 'Invalid uid',
            'data' : {} 
        })


class TodoView(APIView):              #<------- APIView [get, post, put, patch, delete] in one class ----->
    permission_classes = [IsAuthenticated]              
    authentication_classes = [TokenAuthentication]      #Both this class need to Authenticate user
    def get(self, request):
        todo_objs = Todo.objects.filter(user = request.user)   #Shows only details who has login user
        serializer = TodoSerializer(todo_objs, many = True)
        return Response({
                'status' : True,
                'msg' : 'Todo fetched', 
                'data' : serializer.data
            })

    def post(self, request):
        try:
            data = request.data
            data['user'] = request.user.id       # to add which user add data (only works in raw in POSTMAN)
            serializer = TodoSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                'status' : True,
                'msg' : 'success data', 
                'data' : serializer.data
            })
            else:
                return Response({
                    'status' : False,
                    'msg' : 'invalid data', 
                    'data' : serializer.errors
                })

        except Exception as e:
            print(e)
        return Response({
                'status': False,
                'msg': 'Somthing Went Wrong', 
            })


class TodoViewSet(viewsets.ModelViewSet):   #--- with help of view set we can do crud opration with only 2 3 line
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    @action(detail=False, methods=['get'])     #---No need to create URL for action
    def get_timing_todo(self, request):
        objs = TimingTodo.objects.all()
        serializer = TimingTodoSerializer(objs, many=True)
        return Response({
            'status' : True,
            'msg' : 'Timing Todo Fetched',
            'data' : serializer.data
        })

    @action(detail=False, methods=['post'])     #---No need to create URL for action
    def add_date_to_todo(self, request):
        try:
            data = request.data
            serializer = TimingTodoSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status' : True,
                    'message' : 'success data added',
                    'data' : serializer.data
                })
            return Response({
                'status' : False,
                'message' : 'Invalid data',
                'data' : serializer.errors
            })
        except Exception as e:
            print(e)
        return Response({
                'status' : False,
                'message' : 'Somthing went wrong',
            })
        












# @api_view(['GET', 'POST'])
# def prduct_type_api(request):
#     if request.method == 'GET':
#         data = ProductType.objects.all()

#         serializer = ProductTypeSerializers(data, many=True)

#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = ProductTypeSerializers(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['GET', 'POST'])
# def products_details_api(request):
#     if request.method == 'GET':
#         data = Products_Details.objects.all()

#         serializer = Products_DetailsSerializers(data, many=True)

#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = Products_DetailsSerializers(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)            