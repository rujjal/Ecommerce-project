from django.shortcuts import render
from django.views.generic import View
from .models import *


# Create your views here.
# def home(request):
# 	view = {"value":"Hello World"}
# 	return render(request,'index.html',view)

class BaseViews(View):
	views = {}


class HomeView(BaseViews):
	def get(self,request):
		self.views['items'] = Item.objects.all()
		self.views['sale_items'] = Item.objects.filter(labels = 'sale')
		self.views['category'] = Category.objects.all()
		self.views['sliders'] = Slider.objects.all()
		self.views['subcategory'] = SubCategory.objects.all()
		self.views['ad'] = Ad.objects.all()
		self.views['brands'] = Brand.objects.all()

		return render(request, 'index.html', self.views)


class SubCategoryView(BaseViews):
	def get(self,request,slug):
		slug_id = SubCategory.objects.get(slug = slug).id
		self.views['subcat_items'] = Item.objects.filter(subcategory_id = slug_id)

		return render(request, 'index.html', self.views)



