from django.conf.urls import include, url
from django.contrib import admin
from articles import views 


urlpatterns = [
	url(r'^pdf/', views.pdf),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
	url(r'^users/$',  views.users, name='users'),
	url(r'^users/(?P<pk>[0-9]+)/$', views.user_detail, name='user_detail'),
	url(r'^users/new/$', views.user_new, name='user_new'),
	url(r'^users/(?P<pk>[0-9]+)/edit/$', views.user_edit, name='user_edit'),
	url(r'^users/(?P<pk>\d+)/remove/', views.user_remove, name='user_remove'),
]