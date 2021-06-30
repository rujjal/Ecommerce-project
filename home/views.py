from django.shortcuts import render
from django.views.generic import View
from .models import *


# Create your views here.
# def home(request):
# 	view = {"value":"Hello World"}
# 	return render(request,'index.html',view)

class BaseView(View):
	views = {}


class HomeView(BaseView):
	def get(self,request):
		self.views['items'] = Item.objects.all()
		self.views['category'] = Category.objects.all()
		self.views['sliders'] = Slider.objects.all()
		self.views['subcategory'] = SubCategory.objects.all()
		self.views['ad'] = Ad.objects.all()

		return render(request, 'index.html', self.views)


