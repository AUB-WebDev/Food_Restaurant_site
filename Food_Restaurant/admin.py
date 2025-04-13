from django.contrib import admin
from .models import *
from django.utils.html import format_html

admin.site.site_header = "Food Restaurant Admin"
admin.site.site_title = "Food Restaurant Admin Portal"

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
    ordering = ('ProductID',)
    
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
    list_filter = ('ChefPosition',)
    list_per_page = 10
    ordering = ('ChefName',)
    
admin.site.register(Chef, chefAdmin)


class ChefSkillAdmin(admin.ModelAdmin):
    list_display = ('skill_name', 'chef', 'skill_percentage')
    search_fields = ('skill_name', 'chef')
    list_filter = ('chef', 'skill_name')
    list_per_page = 10
    ordering = ('chef',)
    
admin.site.register(ChefSkill, ChefSkillAdmin)

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
    ordering = ('BlogID',)
    
admin.site.register(Blog, blogAdmin)


class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('CatergoryID', 'SocialMediaID', )
    search_fields = ('CatergoryID', 'SocialMediaID')
    list_filter = ('CatergoryID', 'SocialMediaID')
    list_per_page = 10
    ordering = ('CatergoryID',)
    
admin.site.register(SocialMedia, SocialMediaAdmin)


class GalleryAdmin(admin.ModelAdmin):
    def image_preview(self, obj):
        if obj.GalleryImage:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.GalleryImage.url)
        return "No Image"
    image_preview.short_description = 'Image Preview'
    readonly_fields = ["image_preview"]
    list_display = ( 'GalleryName','ProductID', 'image_preview')
    search_fields = ('ProductID', 'GalleryName')
    list_filter = ('ProductID',)
    list_per_page = 10
    ordering = ('ProductID',)
    
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
    list_filter = ('ProductID',)
    list_per_page = 10
    ordering = ('ProductID',)
admin.site.register(SpecialOffer, SpecialOfferAdmin)


class SlideAdmin(admin.ModelAdmin):
    def image_preview(self, obj):
        if obj.SlideThumbnail:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.SlideThumbnail.url)
        return "No Image"
    image_preview.short_description = 'Image Preview'
    readonly_fields = ["image_preview"]
    list_display = ( 'SlideName', 'ProductID','image_preview')
    list_filter = ('ProductID',)
    search_fields = ('SlideName',)
    list_per_page = 10
    ordering = ('ProductID',)
    
admin.site.register(Slide, SlideAdmin)

class faqsAdmin(admin.ModelAdmin):
    list_display = ('Question',)
    search_fields = ('Question',)
    list_filter = ('Question',)
    list_per_page = 10
    ordering = ('Question',)
    
admin.site.register(Faqs, faqsAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('CatergoryID', 'Email', 'PhoneNumber', 'Address', )
    search_fields = ('Email', 'PhoneNumber', 'CatergoryID')
    list_filter = ('CatergoryID',)
    list_per_page = 10
    ordering = ('CatergoryID',)
    
admin.site.register(Contact, ContactAdmin)    



class AboutAdmin(admin.ModelAdmin):
    list_display = ('AboutTitle', 'AboutDescription',)
    search_fields = ('AboutTitle',)
    list_filter = ('AboutTitle',)
    list_per_page = 10
    ordering = ('AboutTitle',)
    
admin.site.register(About, AboutAdmin)

class TemplateAdmin(admin.ModelAdmin):
    list_display = ('TemplateName', 'TemplateID', 'TemplateURL')
    search_fields = ('TemplateName','TemplateID')
    list_filter = ('TemplateName',)
    list_per_page = 10
    ordering = ('TemplateID',)
    
admin.site.register(Template, TemplateAdmin)


class CTAAdmin(admin.ModelAdmin):
    def image_preview(self, obj):
        if obj.CTAImage:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.CTAImage.url)
        return "No Image"
    image_preview.short_description = 'Image Preview'
    readonly_fields = ["image_preview"]
    list_display = ('ProductID', 'image_preview',)
    search_fields = ('ProductID',)
    list_filter = ('ProductID',)
    list_per_page = 10
    ordering = ('ProductID',)
    
admin.site.register(Cta, CTAAdmin)