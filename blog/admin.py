from django.contrib import admin
from .models import Article , Categoreie , Commentaire

class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom_categorie','description')
    search_fields = ('nom_categorie',)
    list_filter = ('date_creation',)

class ArticleAdmin(admin.ModelAdmin):
    list_display= ('titre','date_publication','categorie','auteur','publier')
    search_fields =('titre',)
    list_filter = ('categorie','publier','date_publication')

class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('message','article','username','date_commentaire')
    list_filter = ('date_commentaire',)
# Register your models here.
admin.site.register(Categoreie,CategorieAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Commentaire)


