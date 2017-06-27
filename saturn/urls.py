from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # account
    url(r'account/', include('account.urls')),
    # posts
    url(r'^posts/', include('posts.urls', namespace='posts')),
    # social authentication
    url('social-auth/', include('social_django.urls', namespace='social')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                            document_root=settings.MEDIA_ROOT)


