from django.shortcuts import render
from django.views.generic import View

# Create your views here.
# def home(request):
# 	view = {"value":"Hello World"}
# 	return render(request,'index.html',view)

class BaseView(View):
	views = {}


class HomeView(BaseView):
	def get(self,request):

		return render(request, 'index.html')


