from rest_framework.permissions import AllowAny
from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import APIView
from .models import Approvalmodel
import pandas as pd
from .serializers import Approval1,LoginSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.conf import settings
from django.core.mail import EmailMessage
from joblib import load

from sklearn.preprocessing import LabelEncoder
model_path = r'C:/Users/HP/Desktop/MLPROJECT/MLModels/model.joblib'
ENCODER_PATH = r'C:/Users/HP/Desktop/MLPROJECT/MLModels/label_encoder.joblib'
model = load(model_path)
label_encoder_program = load(r'C:/Users/HP/Desktop/MLPROJECT/MLModels/label_encoder_program.joblib')  # Separate encoder for Program
label_encoder_level = load(r'C:/Users/HP/Desktop/MLPROJECT/MLModels/label_encoder_level.joblib')
# Create your views here.

# class Approval2(generics.ListAPIView,generics.CreateAPIView):
#     queryset=Approvalmodel.objects.all()
#     serializer_class=Approval1
   
#     permission_classes =[AllowAny]
    
    
class Approv(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        data=request.data
        serializer=Approval1(data=data)
        if(serializer.is_valid()):
            serializer.save()
           
            input_data={
                "Program":serializer.data["Program"],
                "Level":serializer.data["Level"],
                "Intake per Division":serializer.data["Intake"],
                "Courses per Division":serializer.data["Courses"],
                "Maximum Intake":serializer.data["Maximum"],
                "Division":serializer.data["Division"],
            }
            print(serializer.data["Email"])
            try:
               input_data['Level'] = label_encoder_level.transform([input_data['Level']])
            except ValueError as e:
                print(f"Error: {e}")
            input_data['Program'] = label_encoder_program.transform([input_data['Program'].split(" ")[0]])
            input_df = pd.DataFrame([input_data])
            prediction = model.predict(input_df)
            if(prediction[0]==0):
                email=serializer.data["Email"]
                emailw=EmailMessage(
                    "Approval For Course",
                    "Your approval has been declined",
                    settings.EMAIL_HOST_USER,
                    [email]
                )
                emailw.send(fail_silently=False)
            else:
                email=serializer.data["Email"]
                emailw=EmailMessage(
                    "Approval For Course",
                    "Your approval has been approved",
                    settings.EMAIL_HOST_USER,
                    [email]
                )
                emailw.send(fail_silently=False)
            return Response({
                "status":"201",
                "data":serializer.data,
                "Prediction":prediction

            })
        return Response({
                "status":"400",
                "data":serializer.errors
            })
    
         
class LoginApi(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        data=request.data
        serializer=LoginSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                "status":False,
                "data":serializer.errors
            })
        username=serializer.data["username"]
        password=serializer.data["password"]

        user_obj=authenticate(username=username,password=password)
        if user_obj:
            token , _=Token.objects.get_or_create(user=user_obj)
            return Response({
                "status":True,
                "data":{'token': str(token)}
            })
        return Response({
            "status":True,
            "data":{}
        })
        





# def list(self, request):
    #     # Note the use of `get_queryset()` instead of `self.queryset`
    #     queryset = self.get_queryset()
    #     serializer = self.get_serializer(queryset, many=True)
    #     processed_data = serializer.data
    #     self.Approval( processed_data)
    #     return Response(processed_data)
    
    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_authenticated:
    #           self.Approval(user)
    #           return user.accounts.all()
    #     else:
    #          return Approvalmodel.objects.none()
    # def Approval(self, user):
    #     print(user