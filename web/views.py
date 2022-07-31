from ctypes import util
from functools import partial
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse 
from .models import client
from .models import Student
from rest_framework.renderers import JSONRenderer 
from .serializer import clientSerializer
from .serializer import StudentSerializer
import io
from rest_framework.parsers import JSONParser
from rest_framework import status
# for csrf bypass
from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators import method_decorator
from django.utils.decorators import method_decorator
from django import views
# from ..response import HttpRespond
# from views import view
# Create your views here.
@csrf_exempt
def index(request):
    mydata = client.objects.get(id= 2)
    serializer = clientSerializer(mydata)
    print(mydata)
    jsonData = JSONRenderer().render(serializer.data)
    return HttpResponse(jsonData, content_type="application\json")  

@csrf_exempt
def createClient(request):
    if request.method == 'POST':
        json_data = request.body
        # print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        # print(json_data)
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = clientSerializer(data = python_data)
        if serializer.is_valid():
            saved_data = serializer.save()
            return_data = clientSerializer(saved_data)
            retun_json = JSONRenderer().render(return_data.data)
            # print(saved_data)
            # res = {'msg': 'Client created Successfully'}
            # json_data = JSONRenderer().render(res)
            return HttpResponse(retun_json, status=status.HTTP_201_CREATED, content_type="application\json")
        return HttpResponse(JSONRenderer().render(serializer.errors), content_type="application\json")
@csrf_exempt
def student(request):
    if request.method == 'GET':
        req_payoad = request.body
        stream = io.BytesIO(req_payoad)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            student = Student.objects.get(id= id)
            serializer = StudentSerializer(student)
            studentJson = JSONRenderer().render(serializer.data)
            return HttpResponse(studentJson, content_type="application\json")
        else:
            student = Student.objects.all()
            serializer = StudentSerializer(student, many=True)
            studentJson = JSONRenderer().render(serializer.data)
            return HttpResponse(studentJson, content_type="application\json")
        
    if request.method == "POST":
        req_payload = request.body
        stream = io.BytesIO(req_payload)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data = python_data)

        if serializer.is_valid():
            saved_data = serializer.save()
            return_data = StudentSerializer(saved_data)
            retun_json = JSONRenderer().render(return_data.data)
            # print(saved_data)
            # res = {'msg': 'Client created Successfully'}
            # json_data = JSONRenderer().render(res)
            return HttpResponse(retun_json, status=status.HTTP_201_CREATED, content_type="application\json")
        return HttpResponse(JSONRenderer().render(serializer.errors), content_type="application\json")
    
    if request.method == 'PUT':
        req_payload = request.body
        stream = io.BytesIO(req_payload)
        python_data = JSONParser().parse(stream)

        id = python_data.get('id')

        student = Student.objects.get(id=id)

        serializer = StudentSerializer(student, data = python_data, partial=True)
        #if giving full data then partial need to be removed

        if serializer.is_valid():
            saved_data = serializer.save()
            return_data = StudentSerializer(saved_data)
            retun_json = JSONRenderer().render(return_data.data)
            return HttpResponse(retun_json, status=status.HTTP_202_ACCEPTED, content_type="application\json")
        return HttpResponse(JSONRenderer().render(serializer.errors), content_type="application\json")

    if request.method == 'DELETE':
        req_payload = request.body
        stream = io.BytesIO(req_payload)
        python_data = JSONParser().parse(stream)

        id = python_data.get('id')

        student = Student.objects.get(id=id)

        deleted_obj = student.delete()
        print(deleted_obj)
        return_data = StudentSerializer(student)
        # retun_json = JSONRenderer().render(return_data.data)
        return JsonResponse(return_data.data, safe=False)
        # return HttpResponse(retun_json, status=status.HTTP_202_ACCEPTED, content_type="application\json")

# for class based view 

@method_decorator(csrf_exempt, name='dispatch')
class studentClass(views):
    def get(self, request, *args, **kwargs):
        req_payoad = request.body
        stream = io.BytesIO(req_payoad)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            student = Student.objects.get(id= id)
            serializer = StudentSerializer(student)
            studentJson = JSONRenderer().render(serializer.data)
            return HttpResponse(studentJson, content_type="application\json")
        else:
            student = Student.objects.all()
            serializer = StudentSerializer(student, many=True)
            studentJson = JSONRenderer().render(serializer.data)
            return HttpResponse(studentJson, content_type="application\json")
    
    # degf post(), def put(), def delete()

        

