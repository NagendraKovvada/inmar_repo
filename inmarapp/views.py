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
from rest_framework import generics
from rest_framework.views import APIView

class UserList(generics.ListCreateAPIView):
	queryset = UserData.objects.all()
	serializer_class = UserSerializer

	def post(self, request, *args, **kwargs):
		serializer = UserSerializer(data=request.data, many=isinstance(request.data, list))
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	# def delete(self, request, *args, **kwargs):
	# 	instance = self.get_object()
	# 	self.perform_destroy(instance)
	# 	return Response(status=status.HTTP_204_NO_CONTENT)

	# def perform_destroy(self, instance):
	#     instance.delete()

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = UserData.objects.all()
	serializer_class = UserSerializer
	lookup_field = 'id'


class UserListView(APIView):
	def get(self, request, format=None):
		users = UserData.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data)

	# def get_queryset(self):
	# 	return UserData.objects.all()
	
	# def destroy(self, request, *args, **kwargs):
	# 	instance = self.get_object()
	# 	self.perform_destroy(instance)
	# 	serializer = UserSerializer
	# 	return Response(serializer.data,status=status.HTTP_201_CREATED)

	# def get_object(self):
	# 	id = self.kwargs.get("id")
	# 	return UserData.objects.get(id=id)

# from django.forms import ModelForm

# class UserList(APIView):

# 	def get(self, request, format=None):
# 		users = UserData.objects.all()
# 		serializer = UserSerializer(users, many=True)
# 		return Response(serializer.data)

# 	def post(self, request, format=None):
# 		serializer = UserSerializer(data=request.DATA)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 	def delete(self, request, SKU, format=None):
# 		import pdb;pdb.set_trace()
# 		user = get_object_or_404(UserData, SKU=SKU)
# 		user.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)

# class UserDetail(APIView):	

# 	def get_object(self, SKU):
# 		# import pdb;pdb.set_trace()
# 		try:
# 			return UserData.objects.get(SKU=SKU)
# 		except UserData.DoesNotExist:
# 			raise Http404

# 	def get(self, request, SKU, format=None):
# 		import pdb;pdb.set_trace()
# 		user = get_object_or_404(UserData, SKU=SKU)
# 		user = UserSerializer(UserData)
# 		return Response(user.data)

# 	def put(self, request, SKU, format=None):
# 		user = get_object_or_404(UserData, SKU=SKU)
# 		serializer = UserSerializer(UserData, data=request.DATA)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 	def delete(self, request, SKU, format=None):
# 		user = get_object_or_404(UserData, SKU=SKU)
# 		user.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)

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

def post_update(request, id, template_name='post_form.html'):
	post = get_object_or_404(UserData, id=id)
	form = UserDataForm(request.POST or None, instance=post)
	if form.is_valid():
		form.save()
		return redirect('post_list')
	return render(request, template_name, {'form': form})

def post_delete(request, id, template_name='post_delete.html'):
	post = get_object_or_404(UserData, id=id)
	if request.method=='POST':
		post.delete()
		return redirect('post_list')
	return render(request, template_name, {'object': post})
# def post_list(request, template_name='post_list.html'):
#     posts = UserData.objects.all()
#     data = {}
#     data['object_list'] = posts
#     return render(request, template_name, data)

# def post_create(request, template_name='post_form.html'):
#     form = UserDataForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('post_list')
#     return render(request, template_name, {'form': form})

# def post_update(request, SKU, template_name='post_form.html'):
#     post = get_object_or_404(UserData, SKU=SKU)
#     form = UserDataForm(request.POST or None, instance=post)
#     if form.is_valid():
#         form.save()
#         return redirect('post_list')
#     return render(request, template_name, {'form': form})

# def post_delete(request, SKU, template_name='post_delete.html'):
#     post = get_object_or_404(UserData, SKU=SKU)
#     if request.method=='POST':
#         post.delete()
#         return redirect('post_list')
#     return render(request, template_name, {'object': post})