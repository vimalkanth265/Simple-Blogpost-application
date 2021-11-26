from django.contrib.messages.api import success

from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.urls.base import reverse_lazy
from .models import BlogPost
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import userregister
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.
def home(request):
    return render(request,'home.html')

def user(request):
    if request.method=='POST':
        form=userregister(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account is created and you can login now')
            return redirect('login')
    else:
        form=userregister()
    return render(request,'signup.html',{'form':form})


@login_required

def profile(request):
     return render(request,'profile.html')


class createview(LoginRequiredMixin, generic.CreateView):
    model=BlogPost
    fields=['Title','Content']
    template_name='create_post.html'
    success_url=reverse_lazy('home')

    def form_valid(self, form) :
        form.instance.Author=self.request.user
        return super().form_valid(form)


class updatepost(LoginRequiredMixin,UserPassesTestMixin, generic.UpdateView):
    model=BlogPost
    fields=['Title','Content']
    template_name='update_post.html'
    success_url=reverse_lazy('home')

    def form_valid(self, form) :
        form.instance.Author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.Author:
            return True
        else:
            return f"Can't access this function"


class deletepost(LoginRequiredMixin, generic.DeleteView):
    model=BlogPost
    template_name='delete_post.html'
    success_url=reverse_lazy('home')

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.Author:
            return True
        else:
            return f"Can't access this function"

    




class Listedview(LoginRequiredMixin,generic.ListView):
    model=BlogPost
    template_name='home.html'
    ordering=['-DatePosted']

class postdetails(generic.DetailView):
    model=BlogPost
    template_name='post_details.html'

    
