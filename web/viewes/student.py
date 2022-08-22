from django.http import HttpResponse, JsonResponse 
from ..models import Student
from ..serializers.student import StudentSerializer
import io
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class studentClass(View):
    
    def get(self, request,id = None, *args, **kwargs):
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
        
    # create student
    def post(self,request, *args, **kwargs):
        req_payload = request.body
        stream = io.BytesIO(req_payload)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data = python_data)
        if serializer.is_valid():
            saved_data = serializer.save()
            return_data = StudentSerializer(saved_data)
            re = {
                "message": 'Created Successfully',
                "data": return_data.data
            }
            retun_json = JSONRenderer().render(re)
            return HttpResponse(retun_json, status=status.HTTP_201_CREATED, content_type="application\json")
        return HttpResponse(JSONRenderer().render(serializer.errors), content_type="application\json")
    
    #update
    def put(self, request, *args, **kwargs):
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
    
    def delete(self, request, *args, **kwargs):
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