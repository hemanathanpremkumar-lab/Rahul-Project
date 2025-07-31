from django.shortcuts import render
from .models import Company,Services,Testimonals,FAQ
from blogapp.models import Blog



# Create your views here.
def home(request):
    company=Company.objects.first()
    service=Services.objects.all()
    testimonals=Testimonals.objects.all()
    faq=FAQ.objects.all()
    recent_post=Blog.objects.order_by('-b_posted_date')[:3]
    # if request.method=='POST':
    

    return render(request,'index.html',{'company':company,'service':service,'testimonals':testimonals,'faq':faq,'recent':recent_post})