from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Blog
from compapp.models import Company

# Create your views here.
def blog(request):
    company=Company.objects.first()
    blog=Blog.objects.all()
    paginator = Paginator(blog,2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request,'blog.html',{'blog':page_obj,'company':company})
 

def blog_details(request,id):
    company=Company.objects.first()
    details=Blog.objects.get(id=id)
    recent_post=Blog.objects.order_by('-b_posted_date')[:2]


    return render(request,'blog-details.html',{'details':details,'company':company,'recent':recent_post})