from django.contrib.auth.models import User
from .models import Message, Forum
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin
from .forms import MessageForm
from django.views.generic import ListView, DetailView, CreateView, View
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Post, Comment, Vote
from django.contrib.auth.views import LogoutView, LoginView
# Create your views here.




class PostListView(ListView):
    model = Post
    template_name = "vote.html"
    context_object_name = "posts"
    ordering = ["-created"]


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ["text"]
    template_name = "comment_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = get_object_or_404(Post, id=self.kwargs["post_id"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"pk": self.kwargs["post_id"]})


class VoteView(LoginRequiredMixin, View):
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        value = int(request.POST.get("value"))

        if value not in [1, -1]:
            return redirect("index")

        Vote.objects.update_or_create(
            user=request.user,
            post=post,
            defaults={"value": value}
        )
        return redirect("index")
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]
    template_name = "post_create.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("index")


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "register.html"
    success_url = reverse_lazy("login")

class ChatView(FormMixin, ListView):
    model = Message
    form_class = MessageForm
    template_name = "chat1.html"
    context_object_name = "messages"
    success_url = reverse_lazy("chat1")

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()  
        text = request.POST.get("text")

        if text:  
            Message.objects.create(text = text, username = request.user)

        return redirect("chat1")

class LogoutView(LogoutView):
    template_name = "logout.html"
    success_url = reverse_lazy("index")
    def get_success_url(self):
        return self.success_url


class LoginView(LoginView):
    template_name = "login.html"
    success_url = reverse_lazy("index")
    def get_success_url(self):
        return self.success_url