from django.contrib import admin
from .models import Item, Article


class ItemAdmin(admin.ModelAdmin):
    list_display = ("title", "publisher", "publish_at")
    list_filter = ("publisher", "publish_at")


admin.site.register(Item, ItemAdmin)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'tag_list', 'username', 'created_at')
    search_fields = ('tags__name', )

    def get_queryset(self, request):
        return super(ArticleAdmin, self).get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())
