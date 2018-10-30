from django.shortcuts import render, redirect
from django.views import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return redirect('/static/index.html')


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return redirect('/static/index.html')
