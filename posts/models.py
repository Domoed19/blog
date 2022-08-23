from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
         related_name="posts",
         blank=True,
         null=True
    )
    image = models.ImageField(upload_to="posts/", blank=True, null=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True
    )
    def __str__(self):
        return f"Post:{self.title}"

class Tag(models.Model):
    title = models.CharField(max_length=100)
    posts = models.ManyToManyField(Post)
    def __str__(self):
        return f"Tag:{self.title} with {self.posts.count()} post(s)"

# class Address(models.Model):
#     author = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         related_name="address",
#         blank=True,
#         null=True
#     )
#     city = models.CharField(max_length=200)
#     address = models.CharField(max_length=200)
#     created_at = models.DateTimeField(
#         auto_now_add=True, db_index=True
#     )
#     def __str__(self):
#         return f"Address:{self.city}, {self.address}"



