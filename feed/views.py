from urllib import request
from django.contrib import messages
from django.views.generic import TemplateView, DetailView, FormView

from feed.models import post

from .forms import PostForm


# Create your views here.

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = post.objects.all().order_by('-id')
        return context


class PostDetailView(DetailView):
    template_name = 'details.html'
    model = post        


class AddPostView(FormView):
    template_name = "new_post.html"
    form_class = PostForm
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        new_object = post.objects.create(
            text = form.cleaned_data['text'],
            image = form.cleaned_data['image'],

        )
        messages.add_message(self.request, messages.SUCCESS, 'Your post was successful')
        return super().form_valid(form)

