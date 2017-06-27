from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                            related_name='posts_created')
    body = models.CharField(max_length=160)
    created = models.DateField(auto_now_add=True, db_index=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='posts_liked',
                                        blank=True)

    def get_absolute_url(self):
        return reverse('posts:detail', args=[self.id])

    def __str__(self):
        return self.title

