"""inmar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib import admin
from inmarapp import views

urlpatterns = [
	url(r'^admin/', admin.site.urls),
    url(r'^rest-auth/', include('rest_auth.urls')),    
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),   
    url(r'^users/', views.UserList.as_view()),
    url(r'^userslist/(?P<id>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^userdel/$', views.UserListView.as_view(), name='userdel'),
    # url(r'^emp/', views.emp),  
    # url(r'^show/',views.show,name='show'),  
    # url(r'^edit/<int:id>', views.edit),  
    # url(r'^update/<int:id>', views.update),  
    # url(r'^delete/<int:id>', views.destroy),
    url(r'^user$', views.post_list, name='post_list'),
    url(r'^new$', views.post_create, name='post_new'),
    url(r'^edit/(?P<id>\d+)$', views.post_update, name='post_edit'),
    url(r'^delete/(?P<id>\d+)$', views.post_delete, name='post_delete'),      
]

