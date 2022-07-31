from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer 

def HttpRespond(serializerData):
    data = JSONRenderer().render(serializerData, content_type="application\json")

