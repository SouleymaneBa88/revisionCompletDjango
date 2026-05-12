from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from .models import Article,Categoreie, Commentaire
from .forms import Commentform
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
class ArticleListView(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name='articles'

class CategorieListView(ListView):
    model = Categoreie 
    template_name = 'categorie.html'
    context_object_name = 'categories'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail_article.html'
    context_object_name = 'article'

    # recuperer les donnees de l'article , commentaire et le formulaire dans un dictionnaire
    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context ['comments'] = Commentaire.objects.filter(article = self.object).order_by('date_commentaire')
        context['form'] = Commentform()
        return context
    
    # pour envoyer les donnes avec une methode car par default il l'envoie avec la methode get 
    def post(self,request,*args,**kwargs):
        self.object = self.get_object()
        form = Commentform(request.POST)

        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.username = request.user
            commentaire.article = self.object
            commentaire.save()
            
            return redirect('detail_article',pk = self.object.pk)
        
        context = self.get_context_data()
        context['form'] = form

        return self.render_to_response(context)
    
class updateCommente(UpdateView):
    model = Commentaire
    form_class = Commentform
    template_name = 'update_comment.html'
    # success_url = reverse_lazy('detail_article')

    def get_success_url(self):
        return reverse('detail_article', kwargs={'pk':self.object.article.pk})
    
class commentDelete(DeleteView):
    model = Commentaire
    template_name = 'delet_comment.html'

    def get_success_url(self):
        return reverse('detail_article', kwargs={'pk':self.object.article.pk})

class Inscription(CreateView):
    form_class = UserCreationForm
    template_name= 'registration/register.html'
    success_url = reverse_lazy('login')
