from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from .models import *
from datetime import datetime

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
        'Gallery': Gallery.objects.all()[:4],
        'Offers': SpecialOffer.objects.all(),
        'Blog' : Blog.objects.all(),
        'Chef' : Chef.objects.all()[:3],
        'About' : About.objects.first(),
        'CTA' : Cta.objects.first(),
    }
    return render(request, 'main/index.html', context)

def viewAbout(request):
    context ={
        'Menu': Menu.objects.all(),
        'SubMenu': SubMenu.objects.all(),
        'Footer' : Footer.objects.all(),
        'Contact' : Contact.objects.first(),
        'Slide' : Slide.objects.all(),
        'Products': Products.objects.all(),
        'Gallery': Gallery.objects.all()[:4],
        'Offers': SpecialOffer.objects.all(),
        'Blog' : Blog.objects.all(),
        'Chef' : Chef.objects.all()[:3],
        'About' : About.objects.first(),
        'CTA' : Cta.objects.first(),
    }
    return render(request, 'main/About.html', context)

def viewService(request):
    context ={
        'Menu': Menu.objects.all(),
        'SubMenu': SubMenu.objects.all(),
        'Footer' : Footer.objects.all(),
        'Contact' : Contact.objects.first(),
        'Slide' : Slide.objects.all(),
        'Products': Products.objects.all(),
        'Gallery': Gallery.objects.all()[:4],
        'Offers': SpecialOffer.objects.all(),
        'Blog' : Blog.objects.all(),
        'Chef' : Chef.objects.all()[:3],
        'About' : About.objects.first(),
        'CTA' : Cta.objects.first(),
    }
    return render(request, 'main/Service.html', context)

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




def viewShop(request):
    context = {
        'Menu': Menu.objects.all(),
        'SubMenu': SubMenu.objects.all(),
        'Footer' : Footer.objects.all(),
        'Contact' : Contact.objects.first(),
        'Products' : Products.objects.all(),
        'Filters' : Products.objects.all()[:5],
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


def viewBlog(request):
    context = {
        'Menu': Menu.objects.all(),
        'SubMenu': SubMenu.objects.all(),
        'Footer' : Footer.objects.all(),
        'Contact' : Contact.objects.first(),
        'Blog' : Blog.objects.all(),
    }
    
    return render(request, 'main/Blog.html', context)




def viewBlogDetail(request, blog_id):
    context = {
        'Menu': Menu.objects.all(),
        'SubMenu': SubMenu.objects.all(),
        'Footer' : Footer.objects.all(),
        'Contact' : Contact.objects.first(),
        'Blog' : Blog.objects.get(BlogID=blog_id),
        'Blogs' : Blog.objects.all(),
    }
    
    return render(request, 'main/Blog-Detail.html', context)


def viewChef(request):
    context = {
        'Menu': Menu.objects.all(),
        'SubMenu': SubMenu.objects.all(),
        'Footer' : Footer.objects.all(),
        'Contact' : Contact.objects.first(),
        'Chef' : Chef.objects.all(),
    }
    
    return render(request, 'main/Chef.html', context)


def viewChefDetail(request, chefname):
    context = {
        'Menu': Menu.objects.all(),
        'SubMenu': SubMenu.objects.all(),
        'Footer' : Footer.objects.all(),
        'Contact' : Contact.objects.first(),
        'Chefs' : Chef.objects.all()[:3],
        'Chef' : Chef.objects.get(ChefName=chefname),
        'ChefSkills' : ChefSkill.objects.filter(chef=chefname),
    }
    
    return render(request, 'main/Chef-Detail.html', context)


def viewTest(request):
    context = {
        'Menu': Menu.objects.all(),
        'SubMenu': SubMenu.objects.all(),
        'Footer' : Footer.objects.all(),
        'Contact' : Contact.objects.first(),
    }
    
    return render(request, 'main/index copy.html', context)

# WishList Structure : {'ProductID': 'DateAdded'}
# Example: {'1': '2023-10-01', '2': '2023-10-02'}

def viewWishlist(request):
    wishlist = request.session.get('wishlist', {})
    wishlist_item = {}
    for key in wishlist.keys():
        product = Products.objects.get(ProductID=key)
        wishlist_item[key] = {
            "Product": product,
            "DateAdded": wishlist[key],
        }
    context = {
        'Menu': Menu.objects.all(),
        'SubMenu': SubMenu.objects.all(),
        'Footer' : Footer.objects.all(),
        'Contact' : Contact.objects.first(),
        'Wishlist' : wishlist_item,
    }
    return render(request, 'main/Wishlist.html', context)


def add_to_wishlist(request, product_id):
    wishlist = request.session.get('wishlist', {})
    if not any(key == str(product_id) for key in wishlist.keys()):
        wishlist[str(product_id)] = datetime.now().strftime("%B-%d-%Y ")
        request.session['wishlist'] = wishlist
    return redirect('wishlist')


def remove_from_wishlist(request, product_id):
    wishlist = request.session.get('wishlist', {})
    if str(product_id) in wishlist.keys():
        wishlist.pop(str(product_id))
        request.session['wishlist'] = wishlist
        if not wishlist:
            del request.session['wishlist']
    request.session.modified = True 
    return redirect('wishlist')



#Cart Structure : {'ProductID': 'Quantity'}
# Example: {'1': 2, '2': 1}

def viewCartlist(request):
    cart = request.session.get('cart', {})
    cart_items = {}
    for key in cart.keys():
        product = Products.objects.get(ProductID=key)
        cart_items[key] = {
            "Product": product,
            "Quantity": cart[key],
            "Subtotal": product.ProductPrice * cart[key],
        }
    total = sum(item["Subtotal"] for item in cart_items.values())
    context = {
        'Menu': Menu.objects.all(),
        'SubMenu': SubMenu.objects.all(),
        'Footer' : Footer.objects.all(),
        'Contact' : Contact.objects.first(),
        'Cart' : cart_items,
        'Total' : total,
    }
    
    return render(request, 'main/Cartlist.html', context)

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart.keys():
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1
    request.session['cart'] = cart
    return redirect('cart')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart.keys():
        cart.pop(str(product_id))
        request.session['cart'] = cart
        if not cart:
            del request.session['cart']
    request.session.modified = True 
    return redirect('cart')

def update_cart(request):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        for key in list(cart.keys()):
            quantity = request.POST.get(f'quantity_{key}')
            if quantity:
                try:
                    quantity = int(quantity)
                    if quantity > 0:
                        cart[key] = quantity
                    else:
                        cart.pop(key, None)
                except ValueError:
                    continue
        
        request.session['cart'] = cart
        request.session.modified = True
    return redirect('cart')

def viewCheckout(request):
    cart = request.session.get('cart', {})
    cart_items = {}
    for key in cart.keys():
        product = Products.objects.get(ProductID=key)
        cart_items[key] = {
            "Product": product,
            "Quantity": cart[key],
            "Subtotal": product.ProductPrice * cart[key],
        }
    total = sum(item["Subtotal"] for item in cart_items.values())
    context = {
        'Menu': Menu.objects.all(),
        'SubMenu': SubMenu.objects.all(),
        'Footer' : Footer.objects.all(),
        'Contact' : Contact.objects.first(),
        'Cart' : cart_items,
        'Total' : total,
    }
    return render(request, 'main/Checkout.html', context)