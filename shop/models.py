from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Cart"),
    (1,"Purchased")
)
default_image = "https://kaxmedia.com/cdn-cgi/image/h=480,w=640/https://objects.kaxmedia.com/auto/o/134882/5596aeb171.jpeg"

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    seller = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    image = models.URLField(null=False, default=default_image)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
