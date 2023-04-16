from django.contrib import admin
from blog.models import (
    CategoryModel,WriteModel,CommentModel
    )


admin.site.register(CategoryModel)

class WritingAdmin(admin.ModelAdmin):
    search_fields = ('title','content')
    list_display = (
        'title','create_time','edit_time'
    )

admin.site.register(WriteModel,WritingAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('yazan','create_time','edit_time')
    search_fields = ('yazan__username',)
    
admin.site.register()    
# Register your models here.
