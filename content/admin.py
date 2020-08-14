from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin

from content.models import CImages, Content


class ContentImageInline(admin.TabularInline):
    model = CImages
    extra = 3


class ContentAdmin(admin.ModelAdmin):
    list_display=['title','type','image_tag','status','create_at']
    list_filter = ['status','type']
    inlines = [ContentImageInline]
    prepopulated_fields = {'slug':('title',)}



admin.site.register(Content,ContentAdmin)