from django.contrib import admin
from blog.models import (
    CategoryModel,WriteModel,CommentModel,CommunicationModel
    )


admin.site.register(CategoryModel)

@admin.register(WriteModel)
class WritingAdmin(admin.ModelAdmin):
    search_fields = ('title','content')
    list_display = (
        'title','create_time','edit_time'
    )


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('yazan','create_time','edit_time')
    search_fields = ('yazan__username',)
    
   
@admin.register(CommunicationModel)
class CommunicationAdmin(admin.ModelAdmin):
    list_display = ('email','create_time')
    search_fields = ('email',)
    
admin.site.register(CommunicationModel,CommunicationAdmin)     
# Register your models here.
