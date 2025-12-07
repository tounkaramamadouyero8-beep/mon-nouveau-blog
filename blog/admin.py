from django.contrib import admin
from django.utils.html import format_html  # ✅ Nouvel emplacement
from .models import Post, Message


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'image_preview')
    readonly_fields = ('image_preview',)
    list_filter = ('published_date', 'author')
    search_fields = ('title', 'text')
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.image.url)
        return "(Pas d'image)"
    image_preview.short_description = 'Aperçu'

class MessageAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'date', 'contenu_court')
    list_filter = ('date',)
    search_fields = ('nom', 'email', 'contenu')
    
    def contenu_court(self, obj):
        return obj.contenu[:50] + "..." if len(obj.contenu) > 50 else obj.contenu
    contenu_court.short_description = 'Contenu'

admin.site.register(Post, PostAdmin)
admin.site.register(Message, MessageAdmin)