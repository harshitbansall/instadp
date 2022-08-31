import base64
import os
import shutil

import instaloader
from django.http import FileResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import InstagramUser

# Create your views here.

class Home(TemplateView):
    def get(self, request):
        return render(request, 'home.html')

class ReturnImage(APIView):
    def post(self, request):
        username = request.data.get('content')
        InstagramUser.objects.create(username=username)
        currentPath = os.getcwd()
        bot = instaloader.Instaloader(quiet = True)
        bot.download_profile(username, profile_pic_only = True)
        for file in os.listdir(username):
            if ".jpg" in file:
                img = base64.b64encode(open("{0}/{1}".format(username,file), 'rb').read())
        shutil.rmtree(username)
        return Response(img)
