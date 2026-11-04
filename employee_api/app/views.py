
from django.views import View
from app.models import Employee
from django.http import JsonResponse
from json import loads
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from app.serializers import EmployeeSerializer
from rest_framework.response import Response

# api view for reading all employee recordsd
class EmployeeList(APIView):
    def get(self,request):
        e=Employee.object_or_404(Employee,id=i)


        serializer_instance=EmployeeSerializer(e)


        return Response(Serializer_instance.data)

#class EmployeeCreate(View):
             
#             def post(self,request):
#                  
#                  form_data=request.body
#                  data=loads(form_data)
#                  e=Employee.objects.create(**data)
#                  e.save()
#                  return JsonResponse({"message":"created"})
       
class EmployeeCreate(APIView):
    def post(self,request):
        #form_data=request.body
        #data=loads(from_data)
        data=request.data     #python native type
        serializer_instance=EmployeeSerializer(data=request.data)#deserialization
        #check whether the request.data is valid if valid the validation
        #data saved to table
        if serializer_instance.is_valid():
            serializer_instance.save()
       
            return Response({"message":"created"})
        #if not valid raise an errors
        else:
        
              return Response(serializer_instance.errors)
