from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import *

# Create your views here.

# NOTE: every view function must contain ['Menu' 'SubMenu' 'Footer' 'Contact'] in the context dictionary
# otherwise it will not work properly

def viewIndex(request):
    context ={
        'Menu': Menu.objects.all(),
        'SubMenu': SubMenu.objects.all(),
        'Footer' : Footer.objects.all(),
        'Contact' : Contact.objects.first(),
        'Slide' : Slide.objects.all(),
        'Products': Products.objects.all(),
        'Gallery': Gallery.objects.all(),
    }
    return render(request, 'main/index.html', context)

def custom_404_view(request, exception):
    return render(request, 'main/404.html', status=404)

def viewFaq(request):
    context = {
        'Menu': Menu.objects.all(),
        'SubMenu': SubMenu.objects.all(),
        'Footer' : Footer.objects.all(),
        'Contact' : Contact.objects.first(),
        'faqs': Faqs.objects.all(),
    }
    return render(request, 'main/faqs.html', context)

def viewContactUs(request):
    context = {
        'Menu': Menu.objects.all(),
        'SubMenu': SubMenu.objects.all(),
        'Footer' : Footer.objects.all(),
        'Contact' : Contact.objects.first(),
    }
    
    return render(request, 'main/ContactUs.html', context)


def viewReservation(request):
    context = {
        'Menu': Menu.objects.all(),
        'SubMenu': SubMenu.objects.all(),
        'Footer' : Footer.objects.all(),
        'Contact' : Contact.objects.first(),
    }
    
    return render(request, 'main/Reservation.html', context)

def viewCheckout(request):
    context = {
        'Menu': Menu.objects.all(),
        'SubMenu': SubMenu.objects.all(),
        'Footer' : Footer.objects.all(),
        'Contact' : Contact.objects.first(),
    }
    
    return render(request, 'main/Checkout.html', context)


def viewWishlist(request):
    context = {
        'Menu': Menu.objects.all(),
        'SubMenu': SubMenu.objects.all(),
        'Footer' : Footer.objects.all(),
        'Contact' : Contact.objects.first(),
    }
    
    return render(request, 'main/Wishlist.html', context)


def viewCartlist(request):
    context = {
        'Menu': Menu.objects.all(),
        'SubMenu': SubMenu.objects.all(),
        'Footer' : Footer.objects.all(),
        'Contact' : Contact.objects.first(),
    }
    
    return render(request, 'main/Cartlist.html', context)


def viewShop(request):
    context = {
        'Menu': Menu.objects.all(),
        'SubMenu': SubMenu.objects.all(),
        'Footer' : Footer.objects.all(),
        'Contact' : Contact.objects.first(),
        'Products' : Products.objects.all(),
    }
    
    return render(request, 'main/Shop.html', context)

def viewShopDetail(request, product_id):
    context = {
        'Menu': Menu.objects.all(),
        'SubMenu': SubMenu.objects.all(),
        'Footer' : Footer.objects.all(),
        'Contact' : Contact.objects.first(),
        'Product' : Products.objects.get(ProductID=product_id),
    }
    
    return render(request, 'main/Shop-Details.html', context)

def viewAccount(request):
    context = {
        'Menu': Menu.objects.all(),
        'SubMenu': SubMenu.objects.all(),
        'Footer' : Footer.objects.all(),
        'Contact' : Contact.objects.first(),
    }
    
    return render(request, 'main/Account.html', context)

def viewGallery(request):
    context = {
        'Menu': Menu.objects.all(),
        'SubMenu': SubMenu.objects.all(),
        'Footer' : Footer.objects.all(),
        'Contact' : Contact.objects.first(),
        'Gallery' : Gallery.objects.all(),
        'Product' : Products.objects.all()[:10]
    }
    
    return render(request, 'main/Gallery.html', context)

def viewTestimonial(request):
    context = {
        'Menu': Menu.objects.all(),
        'SubMenu': SubMenu.objects.all(),
        'Footer' : Footer.objects.all(),
        'Contact' : Contact.objects.first(),
    }
    
    return render(request, 'main/Testimonial.html', context)
