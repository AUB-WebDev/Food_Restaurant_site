from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ('MenuName', 'MenuID', 'TemplateID')
    search_fields = ('MenuName',)
    list_filter = ('TemplateID',)
    list_per_page = 10
    ordering = ('MenuID',)
    
admin.site.register(Menu, MenuAdmin)



class subMenuAdmin(admin.ModelAdmin):
    list_display = ('SubMenuName', 'SubMenuID', 'MenuID', 'TemplateID')
    search_fields = ('SubMenuName',)
    list_filter = ('MenuID', 'TemplateID')
    list_per_page = 10
    ordering = ('SubMenuID',)
    
admin.site.register(SubMenu, subMenuAdmin)


class footerAdmin(admin.ModelAdmin):
    list_display = ('FooterName', 'FooterID', 'TemplateID')
    search_fields = ('FooterName',)
    list_filter = ('TemplateID',)
    list_per_page = 10
    ordering = ('FooterID',)
    
admin.site.register(Footer, footerAdmin) 

class CatergoryAdmin(admin.ModelAdmin):
    def image_preview(self, obj):
        if obj.CatergoryImage:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.CatergoryImage.url)
        return "No Image"
    image_preview.short_description = 'Image Preview'
    readonly_fields = ["image_preview"]
    list_display = ('CatergoryName', 'CatergoryID', 'image_preview')
    search_fields = ('CatergoryName',)
    list_filter = ('CatergoryID',)
    list_per_page = 10
    
    ordering = ('CatergoryID',)
    
admin.site.register(Catergory, CatergoryAdmin)


class ProductsAdmin(admin.ModelAdmin):
    def image_preview(self, obj):
        if obj.ProductImage:
            return format_html('<img src="{}" style="width: 300px; height: auto;" />', obj.ProductImage.url)
        return "No Image"    
    image_preview.short_description = 'Image Preview'
    readonly_fields = ["image_preview"]
    list_display = ('ProductName', 'ProductID', 'ProductPrice', 'CategoryID', 'image_preview')
    search_fields = ('ProductName','ProductID')
    list_filter = ('ProductID', 'CategoryID', 'ProductPrice')
    list_per_page = 10
    
admin.site.register(Products, ProductsAdmin)

class chefAdmin(admin.ModelAdmin):
    def image_preview(self, obj):
        if obj.ChefImage:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.ChefImage.url)
        return "No Image"
    image_preview.short_description = 'Image Preview'
    readonly_fields = ["image_preview"]
    list_display = ('ChefName', 'ChefPosition','image_preview')
    search_fields = ('ChefName',)
    list_per_page = 10
    
admin.site.register(Chef, chefAdmin)


admin.site.register(ChefSkill)

class blogAdmin(admin.ModelAdmin):
    def image_preview(self, obj):
        if obj.BlogThumbnail:
            return format_html('<img src="{}" style="width: 300px; height: auto;" />', obj.BlogThumbnail.url)
        return "No Image"
    image_preview.short_description = 'Image Preview'
    readonly_fields = ["image_preview"]
    list_display = ('BlogTitle', 'BlogID', 'BlogDate', 'image_preview')
    search_fields = ('BlogTitle', 'BlogID')
    list_filter = ('BlogID', 'BlogDate')
    list_per_page = 10
admin.site.register(Blog, blogAdmin)


admin.site.register(SocialMedia)

class GalleryAdmin(admin.ModelAdmin):
    def image_preview(self, obj):
        if obj.GalleryImage:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.GalleryImage.url)
        return "No Image"
    image_preview.short_description = 'Image Preview'
    readonly_fields = ["image_preview"]
    list_display = ( 'GalleryName','ProductID', 'image_preview')
    search_fields = ('ProductID',)
    list_per_page = 10
admin.site.register(Gallery, GalleryAdmin)


class SpecialOfferAdmin(admin.ModelAdmin):
    def image_preview(self, obj):
        if obj.ProductID.ProductImage:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.ProductID.ProductImage.url)
        return "No Image"
    image_preview.short_description = 'Image Preview'
    readonly_fields = ["image_preview"]
    list_display = ( 'ProductID', 'Price','image_preview')
    search_fields = ('ProductID',)
    list_per_page = 10
admin.site.register(SpecialOffer, SpecialOfferAdmin)


class SlideAdmin(admin.ModelAdmin):
    def image_preview(self, obj):
        if obj.SlideThumbnail:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.SlideThumbnail.url)
        return "No Image"
    image_preview.short_description = 'Image Preview'
    readonly_fields = ["image_preview"]
    list_display = ( 'SlideName', 'ProductID','image_preview')
    search_fields = ('SlideName',)
    list_per_page = 10
admin.site.register(Slide, SlideAdmin)

class faqsAdmin(admin.ModelAdmin):
    list_display = ('Question',)
    search_fields = ('Question',)
    list_per_page = 10
admin.site.register(Faqs, faqsAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('CatergoryID', 'Email', 'PhoneNumber', 'Address', )
admin.site.register(Contact, ContactAdmin)    


admin.site.register(About)

class TemplateAdmin(admin.ModelAdmin):
    list_display = ('TemplateName', 'TemplateID', 'TemplateURL')
    search_fields = ('TemplateName',)
    list_per_page = 10
admin.site.register(Template, TemplateAdmin)