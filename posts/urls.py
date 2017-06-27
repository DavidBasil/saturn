from django.conf.urls import url
from . import views


urlpatterns = [
        url(r'create/$', views.post_create, name='create'),
        url(r'^detail/(?P<id>\d+)/$', views.post_detail, name='detail'),
        url(r'like/$', views.post_like, name='like'),
        url(r'^$', views.post_list, name='list')
        ]
