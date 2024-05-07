from myapp.models import Blog, Category, CommentBlog
from django.contrib import admin

@admin.register(Category)
class RegistrationBlog(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Blog)
class RegistrationBlog(admin.ModelAdmin):
    list_display = ['id','author','title','category']

@admin.register(CommentBlog)
class RegistrationComent(admin.ModelAdmin):
    list_display = ['id','new_comment','asked_by','asked_at']

admin.site.site_title="Administration"
admin.site.index_title="Blogger Adda"
admin.site.site_header="Blogger's Adda Administration "

