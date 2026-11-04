from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from app.serializers import DoctorSerializer
from app.models import Doctor
class DoctorListCreate(APIView):


    def get(self,request):
        d=Doctor.objects.all()
        serializer_instance=DoctorSerializer(d,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

            





    
    def post(self,request):
        #creating a new doctor record
        serializer_instance=DoctorSerializer(data=request.data)
        if serializer_instance.is_valid():

            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

       
   
class DoctorRetrieveUpdateDelete(APIView):
    def get(self,request,id):

        d=get_object_or_404(Doctor,id=id)
        serializer_instance=DoctorSerializer(d)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

        
    def put(self,request,id):
        d=get_object_or_404(Doctor,id=id)
        serializer_instance=DoctorSerializer(instance=d,data=request.data)
        if serializer_instance.is_valid():
             serializer_instance.save()
             return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
             return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)  

    
    def delete(self,request,id):
        d=get_object_or_404(Doctor,id=id)
        d.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



        