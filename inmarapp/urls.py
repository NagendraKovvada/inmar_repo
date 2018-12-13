from django.conf.urls import include,url
from inmarapp.views import UserDetails,UserDetail


urlpatterns =('',
    url(r'^userdetails/', UserDetails.as_view()),
    url(r'^del/(?P<id>[0-9]+)/$',UserDetail.as_view()),
    # url(r'^emp/', views.emp),  
    # url(r'^show/',views.show,name='show'),  
    # url(r'^edit/<int:id>', views.edit),  
    # url(r'^update/<int:id>', views.update),  
    # url(r'^delete/<int:id>', views.destroy),
    url(r'^user$', views.post_list, name='post_list'),
    url(r'^new$', views.post_create, name='post_new'),
    url(r'^edit/(?P<id>\d+)$', views.post_update, name='post_edit'),
    url(r'^delete/(?P<id>\d+)$', views.post_delete, name='post_delete'),
    
    
)
