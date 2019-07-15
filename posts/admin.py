from django.contrib import admin

# Register your models here.


from .models import Post

class PostModuleAdmin(admin.ModelAdmin):
    list_display=["__str__", "timepublish"]
    list_display_links=["__str__", "timepublish"]
    list_filter = ["timepublish"]
    search_fields = ["title", "content"]

    class Meta:
        model=Post


admin.site.register(Post, PostModuleAdmin)


