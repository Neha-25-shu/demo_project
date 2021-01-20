from django.db.models import Count, Q
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import (
    View,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView,
)
from .forms import CommentForm, PostForm, Contactform
from .models import Post, Author, PostView
from marketing.forms import EmailSignupForm
from marketing.models import Signup

form = EmailSignupForm()


def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None


class SearchView(View):
    def get(self, request, *args, **kwargs):
        queryset = Post.objects.all()
        query = request.GET.get("q")
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(overview__icontains=query)
            ).distinct()
        context = {"queryset": queryset}
        return render(request, "search_results.html", context)


def search(request):
    queryset = Post.objects.all()
    query = request.GET.get("q")
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) | Q(overview__icontains=query)
        ).distinct()
    context = {"queryset": queryset}
    return render(request, "search_results.html", context)


def get_category_count():
    queryset = Post.objects.values("categories__title").annotate(
        Count("categories__title")
    )
    return queryset


class IndexView(View):
    form = EmailSignupForm()

    def get(self, request, *args, **kwargs):
        featured = Post.objects.filter(featured=True)
        latest = Post.objects.order_by("-timestamp")[0:3]
        context = {"object_list": featured,
                   "latest": latest, "form": self.form}
        return render(request, "index.html", context)

    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
        messages.info(request, "Successfully subscribed")
        return redirect("home")


class Contact_form_view(FormView):
    form_class = Contactform
    success_url = "contact"
    template_name = "contact.html"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class PostListView(ListView):
    form = EmailSignupForm()
    model = Post
    template_name = "blog.html"
    context_object_name = "queryset"
    paginate_by = 1

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        most_recent = Post.objects.order_by("-timestamp")[:3]
        context = super().get_context_data(**kwargs)
        context["most_recent"] = most_recent
        context["page_request_var"] = "page"
        context["category_count"] = category_count
        context["form"] = self.form
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = "post.html"
    context_object_name = "post"
    form = CommentForm()

    def get_object(self):
        obj = super().get_object()
        if self.request.user.is_authenticated:
            PostView.objects.get_or_create(user=self.request.user, post=obj)
        return obj

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        most_recent = Post.objects.order_by("-timestamp")[:3]
        context = super().get_context_data(**kwargs)
        context["most_recent"] = most_recent
        context["page_request_var"] = "page"
        context["category_count"] = category_count
        context["form"] = self.form
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse("post-detail", kwargs={"pk": post.pk}))


class PostCreateView(CreateView):
    model = Post
    template_name = "post_create.html"
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create"
        return context

    def form_valid(self, form):
        form.instance.author = get_author(self.request.user)
        form.save()
        return redirect(reverse("post-detail", kwargs={"pk": form.instance.pk}))


class PostUpdateView(UpdateView):
    model = Post
    template_name = "post_create.html"
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update"
        return context

    def form_valid(self, form):
        form.instance.author = get_author(self.request.user)
        form.save()
        return redirect(reverse("post-detail", kwargs={"pk": form.instance.pk}))


class PostDeleteView(DeleteView):
    model = Post
    success_url = "/blog"
    template_name = "post_confirm_delete.html"
