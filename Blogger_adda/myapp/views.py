from django.contrib.auth.forms import PasswordChangeForm
from myapp.form import BloggerLogin, BloggerRegistration, ChangeMyPass, CommentForm, UploadBlog
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Blog, Category, CommentBlog
from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        form = BloggerRegistration(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            form = BloggerRegistration()
            return redirect("home")
        else:
            print("form is not valid")
            for field in form:
                print("Field Error:", field.name,  field.errors)
            form = BloggerRegistration()
    else:
        form = BloggerRegistration()
    return render(request, 'Register.html', {'form':form})

def blogin(request):
    form = BloggerLogin()
    if request.method == 'POST':
        uname = request.POST['username']
        upass = request.POST['password']
        user = authenticate(username=uname,password=upass)
        if user is None:
            messages.error(request,'Please Enter Correct Credinatial')
            return redirect('login')
        else:
            login(request,user)
        return redirect('home')
    else:
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return render(request,'Login.html',{'form':form})

@login_required(login_url='login')
def new_blog(request):
    form = UploadBlog(request.POST,request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('home')
        else:
            print("Form is not valid")
    else:
        form = UploadBlog()
    return render(request,'new_blog.html',{'form':form})

@login_required(login_url='login')
def my_blogs(request):
    if request.method == 'POST':
        all_data = Blog.objects.filter(author=request.user)
        form = UploadBlog(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'My_blog.html',{'blogs':all_data,'form':form})
    else:
        form = UploadBlog()
        all_data = Blog.objects.filter(author=request.user)
    return render(request,'My_blog.html',{'all_data':all_data,'form':form})

def UpdateView(request,id):
    if request.method == 'POST':
        data = Blog.objects.get(id=id)
        form = UploadBlog(request.POST,request.FILES,instance=data)
        all_data = Blog.objects.filter(author=request.user)
        if form.is_valid():
            ink = form.save(commit=False)
            ink.author = request.user
            ink.save()
            messages.success(request,'Blog updated successfully...')
            return redirect('my_blogs')
        else:
            data = Blog.objects.get(id=id)
            form = UploadBlog(instance=data)
            all_data = Blog.objects.filter(author=request.user)
    else:
        data = Blog.objects.get(id=id)
        form = UploadBlog(instance=data)
        all_data = Blog.objects.filter(author=request.user)
    context = {'form':form,'all_data':all_data,'data':data}
    return render(request,'My_blog.html',context)

    

def deleteView(request,id):
    data = Blog.objects.get(id=id)
    data.delete()
    return redirect('my_blogs')


@login_required(login_url='login')
def deleteaccview(request):
    if request.user.is_authenticated:
        u = User.objects.get(id=request.user.id)
        u.delete()
        return redirect('home')
    else:
        messages.info(request,"Login first...!!!")
        return redirect('login')


@login_required(login_url='login')
def changepassview(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form = ChangeMyPass(user = request.user, data = request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            form = ChangeMyPass(user = request.user)
        context= {'form':form}
        return render(request,'Change_pass.html',context)

@login_required(login_url='login')
def blogout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request,"You have logged out...!!!")
        return redirect('login')
    else:
        messages.info(request,"Login first...!!!")
        return redirect('login')

def filter_cat(request,id):
    all_data=Blog.objects.filter(category=Category.objects.get(id=id))
    return render(request,"blogs.html",{"all_data":all_data})

@login_required(login_url='login')
def blog_detail(request,id):
    form=CommentForm()
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.blog=Blog.objects.get(id=id)
            instance.asked_by=User.objects.get(id=request.user.id)
            instance.save()
            return redirect('/blog_detail/'+str(id))
        else:
            form=CommentForm()
            print("Form is not valid")
    all_data=Blog.objects.get(id=id)
    liked = all_data.like.filter(id=request.user.id).exists()
    no_of_likes= all_data.number_of_likes()
    all_comm=CommentBlog.objects.filter(blog=all_data)
    all_comm=all_comm.order_by('-asked_at')
    return render(request,"blogs_details.html",{"blog":all_data,'liked':liked,"no_of_likes":no_of_likes,"form":form,'all_comm':all_comm})


def LikePostView(request,id):
    all_data=Blog.objects.get(id=id)
    if all_data.like.filter(id=request.user.id).exists():
        all_data.like.remove(request.user)
        return redirect('/blog_detail/'+str(id))
    else:
        all_data.like.add(request.user)
        
        return redirect('/blog_detail/'+str(id))

def all_blogs(request):
    data=Blog.objects.order_by('-id')
    return render(request,'blogs.html',{'all_data':data,})

def ret_home(request):
    cat = Category.objects.all()
    return render(request,'Home.html',{'cat':cat})

def support(request):
    return render(request,"support.html")

def view_comment(request,id):
    curr_blog=Blog.objects.get(id=id)
    all_comment=CommentBlog.objects.filter(blog=curr_blog)
    return render(request,"edit_comment.html",{"all_comment":all_comment})

def user_comment(request):
    all_comment=CommentBlog.objects.filter(asked_by=request.user)
    exist=all_comment.exists()
    return render(request,"my_comment.html",{"all_comment":all_comment,"exist":exist})

def deleteCommentView(request,id):
    obj=CommentBlog.objects.get(id=id)
    obj.delete()
    
    return redirect('my_blogs')