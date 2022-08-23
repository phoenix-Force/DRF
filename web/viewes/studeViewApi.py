from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
# from rest_framework.response import Response


from ..models import Student
from ..serializers.student import StudentSerializer



@api_view(['GET', 'POST'])
def getStudent(request, id = None):
    if request.method == 'GET':
        if id is not None:
            student = Student.objects.get(id= id)
            serializer = StudentSerializer(student)
            return Response({'message': 'Successfull', 'data': serializer.data}, content_type="application\json")
        else:
            student = Student.objects.all()
            serializer = StudentSerializer(student, many=True)
            return Response({'message': 'Successfull', 'data': serializer.data}, content_type="application\json")
