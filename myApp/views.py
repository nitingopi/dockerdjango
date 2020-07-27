from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.
from django.http import HttpResponse
class Home(APIView):
    def get(self, request):
        return HttpResponse(" Django on Docker on AWS ")