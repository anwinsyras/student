from rest_framework import serializers
from rest_framework.views import APIView
class EmployeeSerializer(serializers.Serializer):
        id=serializers.IntegerField(read_only=True)

        gender_choices = (('male', 'MALE'),('female', 'FEMALE'))
    
        empid = serializers.IntegerField()
        name = serializers.CharField(max_length=10)
        age = serializers.IntegerField()
        gender = serializers.ChoiceField(choices=gender_choices)
        salary = serializers.IntegerField()
        designation = serializers.CharField(max_length=20)
        joining_date = serializers.DateField(read_only=True)


        #employee serializer used to convert employee data

        #after validation and before saving
        def create(self,validated_data):
                print(validated_data)
                e=Employee.objects.create(**validated_data)#create employee record
                e.save()#saves in db table employee
                return e

        #employee serializer used to convert employee data
        class EMployeeRetrieve(APIView):
                def get(self,request,i):#parameters recieves the id coming from client side
                        e=Employee.object.get(id=1)   #model object(django format)
                        #converts the model object into python native type using EmployeeSerializer

                        serializer_instance=EmployeeSerializer(e)
                        #sends the response back to clinet
                        return Response(serializer_instance.data)

def create(sled,validate_data):
        u=User.objects.create_user(**validate_data)
        u.save()
        send_mail(subject="welcome to employee app",
                  message="thankyou signing up for an account",
                  from_email="anwinsyras12@gmail.com",
                  reciepient_list=[u.email,],
                  fail_silently=True)
        return u          