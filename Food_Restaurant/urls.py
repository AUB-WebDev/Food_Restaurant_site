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
]
