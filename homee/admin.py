from django.contrib import admin, messages
from .models import *
from django.utils.safestring import mark_safe

# class FilterPost(admin.SimpleListFilter):
#     title = "Filter posts"
#     parameter_name = 'status'

#     def lookups(self, request, model_admin):
#         return [
#             ('DRAFT', 'Not Published'),
#             ('PUBLISHED', 'Published'),
#         ]

#     def queryset(self, request, queryset):
#         return queryset

@admin.register(Home)
class McAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'photo', 'post_photo', 'about', 'tags', 'cat']
    readonly_fields = [ 'slug', 'post_photo']
    #filter_horizontal = ['tags']
    #filter_vertical = ['tags']
    list_display = ('title', 'post_photo', 'time', 'is_published', 'cat')
    list_display_links = ('title', )
    ordering = ['-time', 'likes']
    list_editable = ('is_published', )
    list_per_page = 5
    actions = ['set_published', 'set_draft']
    search_fields = ['title__startswith']
    list_filter = ['cat__name', 'is_published']

    save_on_top = True

    @admin.display(description="Image")
    def post_photo(self, home: Home):
        if home.photo:
            return mark_safe(f'<img src="{home.photo.url}" width=50>')
        else:
            return 'No photo!'
    
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Home.Status.PUBLISHED)
        self.message_user(request, f"{count} data updated!")

    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Home.Status.DRAFT)
        self.message_user(request, f"{count} data set to draft!", messages.WARNING)


@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(TagPost)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag', 'slug')
    list_display_links = ('id', 'tag')

admin.site.register(Comment)
admin.site.register(Reply)