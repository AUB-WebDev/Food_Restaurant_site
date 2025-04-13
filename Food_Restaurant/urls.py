from . import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('', views.viewIndex, name='home'),
    path('faqs/', views.viewFaq, name='faqs'),
    path('contact/', views.viewContactUs, name='contact'),
    path('reservation/', views.viewReservation, name='reservation'),
    path('checkout/', views.viewCheckout, name='checkout'),
    path('wishlist/', views.viewWishlist, name='wishlist'),
    path('cart/', views.viewCartlist, name='cart'),
    path('shop/', views.viewShop, name='shop'),
    path('shopdetail/<int:product_id>/', views.viewShopDetail, name='shopdetail'),
    path('account/', views.viewAccount, name='account'),
    path('gallery/', views.viewGallery, name='gallery'),
    path('testimonial', views.viewTestimonial, name='testimonial'),
    path('blog/', views.viewBlog, name='blog'),
    path('blogdetail/<int:blog_id>/', views.viewBlogDetail, name='blogdetail'),
    path('chef/', views.viewChef, name='chef'),
    path('chefdetail/<str:chefname>/', views.viewChefDetail, name='chefdetail'),
    path('about/', views.viewAbout, name='about'),
    path('service/', views.viewService, name='service'),
    path('test', views.viewTest, name='test'),
    path('wishlist/add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/', views.update_cart, name='update_cart'),
]
