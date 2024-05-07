
from myapp.views import LikePostView, UpdateView,blog_detail, all_blogs, blogin, blogout, changepassview, deleteCommentView, deleteView, deleteaccview, filter_cat, my_blogs, new_blog, register, ret_home,deleteaccview, support, user_comment, view_comment
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',register,name='register'),
    path('home/',ret_home,name='home'),
    path('login/',blogin,name='login'),
    path('logout/',blogout,name='logout'),
    path('new_blog/',new_blog,name='new_blog'),
    path('my_blogs/',my_blogs,name='my_blogs'),
    path('update/<int:id>/',UpdateView,name='update'),
    path('delete/<int:id>/',deleteView,name='delete'),
    path('deleteacc/',deleteaccview,name="deleteacc"),
    path('changepass/',changepassview,name='changepass'),
    path('blogs/<int:id>',filter_cat,name='blogs'),
    path('allblogs/',all_blogs,name='all_blogs'),
    path("support/",support,name='support'),
    path("blog_detail/<int:id>",blog_detail,name='blog_detail'),
    path("comments/<int:id>",view_comment,name='comments'),
    path("mycomments/",user_comment,name='mycomments'),
    path("deletecomments/<int:id>",deleteCommentView,name='deletecomments'),
    
    path('likepost/<int:id>/',LikePostView,name="likepost")

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
