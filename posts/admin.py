from django.contrib import admin

# Register your models here.


from .models import Post, Project, Human, Comments


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


class HumanModuleAdmin(admin.ModelAdmin):
    list_display = ["__str__", "name", "surname"]
    list_display_links = ["__str__", "name", "surname"]
    list_filter = ["name"]
    search_fields = ["name", "surname"]

    class Meta:
        model = Human


admin.site.register(Post, PostModuleAdmin)
admin.site.register(Project, ProjectModuleAdmin)
admin.site.register(Human, HumanModuleAdmin)


