from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='images/',null=True,blank=True,default='images/defaultimg.jpg')
    def __str__(self):
        return self.name

class Blog(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    img = models.ImageField(upload_to='images/',null=True,blank=True,default='images/defaultimg.jpg')
    
    like = models.ManyToManyField(User, related_name='blogpost_like',blank=True)

    def __str__(self):
        return self.title
    
    def number_of_likes(self):
        return self.like.count()

class CommentBlog(models.Model):
    new_comment = models.CharField(max_length=1000)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    asked_by = models.ForeignKey(User,on_delete=models.CASCADE)
    asked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.new_comment

