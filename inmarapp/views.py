from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
from .models import UserData
from django.http import Http404
from django.shortcuts import render, redirect,get_object_or_404
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .forms import UserDataForm  


# from django.forms import ModelForm

class UserList(APIView):

	def get(self, request, format=None):
		users = UserData.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = UserSerializer(data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, SKU, format=None):
		import pdb;pdb.set_trace()
		user = get_object_or_404(UserData, SKU=SKU)
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class UserDetail(APIView):	

	def get_object(self, SKU):
		# import pdb;pdb.set_trace()
		try:
			return UserData.objects.get(SKU=SKU)
		except UserData.DoesNotExist:
			raise Http404

	def get(self, request, SKU, format=None):
		import pdb;pdb.set_trace()
		user = get_object_or_404(UserData, SKU=SKU)
		user = UserSerializer(UserData)
		return Response(user.data)

	def put(self, request, SKU, format=None):
		user = get_object_or_404(UserData, SKU=SKU)
		serializer = UserSerializer(UserData, data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, SKU, format=None):
		user = get_object_or_404(UserData, SKU=SKU)
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

# def emp(request):
# 	if request.method == "POST":
# 		form = UserDataForm(request.POST)
# 		if form.is_valid():			
# 			try:
# 				form.save()
# 				return redirect('/show/')
# 			except:
# 				pass
# 		else:
# 			form = UserDataForm()
# 	return render(request,'index.html',{'form':form})  
# def show(request):
# 	sku = UserData.objects.all()
# 	return render(request,"show.html",{'skudata':sku})
# def edit(request, id):
# 	import pdb;pdb.set_trace()
# 	sku = UserData.objects.get(id=id)
# 	return render(request,'edit.html', {'skudata':sku})  
# def update(request, id):
# 	sku = UserData.objects.get(id=id)
# 	form = UserDataForm(request.POST, instance = sku)
# 	if form.is_valid():
# 		form.save()
# 		return redirect("/show")
# 	return render(request, 'edit.html', {'skudata': sku})  
# def destroy(request, id):
# 	import pdb;pdb.set_trace()
# 	sku = UserData.objects.get(id=id)
# 	sku.delete()
# 	return redirect("/show")


# Create your views here.

# class PostsForm(ModelForm):
#     class Meta:
#         model = blog_posts
#         fields = ['id', 'title', 'author']

def post_list(request, template_name='post_list.html'):
    posts = UserData.objects.all()
    data = {}
    data['object_list'] = posts
    return render(request, template_name, data)

def post_create(request, template_name='post_form.html'):
    form = UserDataForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('post_list')
    return render(request, template_name, {'form': form})

def post_update(request, SKU, template_name='post_form.html'):
    post = get_object_or_404(UserData, SKU=SKU)
    form = UserDataForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('post_list')
    return render(request, template_name, {'form': form})

def post_delete(request, SKU, template_name='post_delete.html'):
    post = get_object_or_404(UserData, SKU=SKU)
    if request.method=='POST':
        post.delete()
        return redirect('post_list')
    return render(request, template_name, {'object': post})