from django.contrib import admin
from blog.models import CategoryModel,WriteModel

admin.site.register(CategoryModel)

class WritingAdmin(admin.ModelAdmin):
    search_fields = ('title','content')
    list_display = (
        'title','create_time','edit_time'
    )

admin.site.register(WriteModel,WritingAdmin)
# Register your models here.
