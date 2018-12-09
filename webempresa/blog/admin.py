from django.contrib import admin
from .models import Category, Post
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories')
    ordering = ('author', 'published')
    search_fields = ('title','content', 'author__username', 'categories__name')
    date_hierarchy = 'published'
    list_filter = ('author','categories__name',)

    def post_categories(self, obj):
        result = ""
        for categoria in obj.categories.all():
            result+= categoria.name
            result+= ", "
        return result
    post_categories.short_description = "Categorías"
    





