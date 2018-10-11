from django.shortcuts import render
from django.http import HttpResponse
def index(request):
	context = {}
	print("start")
	if request.GET.get('activate'):
		print("button pressed")
	return render(request, 'ffotf/index.html',context)
def action(request):
	context ={}
	exec(open("start.py").read())
	return render(request,'ffotf/activate.html',context)
# Create your views here.
