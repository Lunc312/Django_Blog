from django.contrib import admin

# Register your models here.


from .models import Post, Project, Comments


class PostInline(admin.StackedInline):
    model = Comments


class PostModuleAdmin(admin.ModelAdmin):
    inlines = [PostInline]
    list_display=["__str__", "timepublish"]
    list_display_links=["__str__", "timepublish"]
    list_filter = ["timepublish"]
    search_fields = ["title", "content"]

    class Meta:
        model = Post


class ProjectModuleAdmin(admin.ModelAdmin):
    search_fields = ["title", "content"]

    class Meta:
        model = Project


admin.site.register(Post, PostModuleAdmin)
admin.site.register(Project, ProjectModuleAdmin)


