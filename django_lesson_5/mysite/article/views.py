from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from account.models import Profile
from .mixins import FormMessageMixin
from django.db.models import Q
from django.utils.translation import get_language, activate

class IndexView(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'articles'
    paginate_by = 20

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Article.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        return Article.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['page_title'] = 'All titles'
        return context


class ArticleCreateView(FormMessageMixin, CreateView):
    model = Article
    template_name = 'article/create.html'
    form_class = ArticleForm
    form_valid_message = 'Article created successfully!'

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        form.instance.author = profile
        return super(ArticleCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('detail', args=(self.object.id,))


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/detail.html'
    context_object_name = 'article'
    pk_url_kwarg = 'article_id'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data()
        context['language'] = get_language()
        return context


class ArticleUpdateView(FormMessageMixin, UpdateView):
    model = Article
    template_name = 'article/update.html'
    form_class = ArticleForm
    pk_url_kwarg = 'article_id'
    form_valid_message = 'Updated successfully!'

    def get_success_url(self):
        return reverse('detail', args=(self.object.id,))


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = '/'
    pk_url_kwarg = 'article_id'
    template_name = 'article/confirm_delete.html'
    context_object_name = 'article'
    

class CommentListView(ListView):
    model = Comment
    template_name = 'article/detail.html'
    context_object_name = 'comment'


class CommentCreateView(FormMessageMixin, CreateView):
    model = Comment
    template_name = 'article/create_comment.html'
    form_class = CommentForm
    form_valid_message = 'Comment created successfully!'
    # pk_url_kwarg = 'article_id'

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        article = Comment.objects.filter(pk=self.object)
        form.instance.user = profile
        form.instance.article = article
        return super(CommentCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('detail', args=(self.object.id,))
