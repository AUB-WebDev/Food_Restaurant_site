from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Menu(models.Model):
    MenuName = models.CharField(max_length=40)
    MenuID = models.BigAutoField(primary_key=True)
    TemplateID = models.ForeignKey('Template', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.MenuName + " - ( " + str(self.MenuID) + " )"
    
class SubMenu(models.Model):
    SubMenuName = models.CharField(max_length=40)
    SubMenuID = models.BigAutoField(primary_key=True)
    MenuID = models.ForeignKey('Menu', on_delete=models.CASCADE)
    TemplateID = models.ForeignKey('Template', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.SubMenuName + " - ( " + str(self.SubMenuID) + " )"
    
class Footer(models.Model):
    FooterName = models.CharField(max_length=40)
    FooterID = models.BigAutoField(primary_key=True)
    TemplateID = models.ForeignKey('Template', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.FooterName + " - ( " + str(self.FooterID) + " )"
    
class Catergory(models.Model):
    CatergoryName = models.CharField(max_length=60)
    CatergoryID = models.BigAutoField(primary_key=True)
    CatergoryImage = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.CatergoryName + " - ( " + str(self.CatergoryID) + " )"
    
class Products(models.Model):
    ProductName = models.CharField(max_length=100)
    ProductID = models.BigAutoField(primary_key=True)
    ProductPrice = models.FloatField()
    ProductImage = models.ImageField(upload_to='images/')
    ProductText = models.TextField(max_length=500, null=True, blank=True)
    ProductDescription = models.TextField(max_length=500, null=True, blank=True)
    CategoryID = models.ForeignKey('Catergory', on_delete=models.CASCADE)

    def __str__(self):
        return self.ProductName + " - ( " + str(self.ProductID) + " )"
    
class Blog(models.Model):
    BlogTitle = models.CharField(max_length=100)
    BlogID = models.BigAutoField(primary_key=True)
    BlogDescription = RichTextUploadingField(null=True, blank=True)
    BlogThumbnail = models.ImageField(upload_to='images/')
    BlogDate = models.DateTimeField(auto_now_add=True)
    BlogAuthor = models.CharField(max_length=50, null=True, blank=True)
    Tags = models.CharField(max_length=100, null=True, blank=True)
    CatergoryID = models.ForeignKey('Catergory', on_delete=models.CASCADE)

    def __str__(self):
        return self.BlogTitle + " - ( " + str(self.BlogID) + " )"
    
class Chef(models.Model):
    ChefName = models.CharField(max_length=100, primary_key=True)
    ChefImage = models.ImageField(upload_to='images/')
    ChefPosition = models.CharField(max_length=100, null=True, blank=True)
    ChefDescription = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.ChefName 
    
class ChefSkill(models.Model):
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE, related_name='skills')
    skill_name = models.CharField(max_length=100)
    skill_percentage = models.PositiveIntegerField()  # stores 0-100
    
    def __str__(self):
        return f"{self.chef.ChefName} - {self.skill_name} ({self.skill_percentage}%)"

class SocialMedia(models.Model):
    CatergoryID = models.ForeignKey('Catergory', on_delete=models.CASCADE)
    SocialMediaURL = models.CharField(max_length=300, null=True, blank=True)
    SocialMediaID = models.ForeignKey('Chef', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.SocialMediaID.ChefName + " - ( " + str(self.CatergoryID.CategoryName) + " )"


class Gallery(models.Model):
    GalleryName = models.CharField(max_length=100, null=True, blank=True)
    GalleryImage = models.ImageField(upload_to='images/')
    ProductID = models.ForeignKey('Products', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.GalleryName + " - ( " + str(self.ProductID) + " )"
    
class SpecialOffer(models.Model):
    ProductID = models.ForeignKey('Products', on_delete=models.CASCADE)
    Price = models.FloatField()
    OfferImage = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.ProductID.ProductName + " - ( " + str(self.Price) + " )"
    
class Slide(models.Model):
    SlideName = models.CharField(max_length=100, null=True, blank=True)
    SlideBGImage = models.ImageField(upload_to='images/', null=True, blank=True)
    SlideThumbnail = models.ImageField(upload_to='images/')
    ProductID = models.ForeignKey('Products', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.SlideName + " - ( " + str(self.ProductID) + " )"
    
class Faqs(models.Model):
    Question = models.CharField(max_length=200)
    Answer = models.TextField(max_length=500)
    Image = models.ImageField(upload_to='images/', null=True, blank=True)
    
    def __str__(self):
        return self.Question 
    
class Contact(models.Model):
    Address = models.CharField(max_length=200)
    Email = models.EmailField()
    PhoneNumber = models.CharField(max_length=20)
    OpenHour  = models.CharField(max_length=100)
    CatergoryID = models.ForeignKey('Catergory', on_delete=models.CASCADE)
    
    def __str__(self):
        return 'Contact Info'
    
class About(models.Model):
    AboutTitle = models.CharField(max_length=100)
    AboutDescription = RichTextUploadingField(null=True, blank=True)
    AboutLeftBG = models.ImageField(upload_to='images/')
    AboutRightBG = models.ImageField(upload_to='images/')
    AboutLeftThumbnail = models.ImageField(upload_to='images/')
    AboutRightThumbnail = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return "About US"


class Template(models.Model):
    TemplateID = models.BigAutoField(primary_key=True)
    TemplateName = models.CharField(max_length=100)
    TemplateURL = models.CharField(max_length=300)
    def __str__(self):
        return self.TemplateName+" - ( " + str(self.TemplateID) + " )"
    
class Cta(models.Model):
    ProductID = models.ForeignKey('Products', on_delete=models.CASCADE)
    CTAImage = models.ImageField(upload_to='images/')
    CTABg = models.ImageField(upload_to='images/')
    
    
class Wishlist(models.Model):
    ProductID = models.ForeignKey('Products', on_delete=models.CASCADE)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    
class Cart(models.Model):
    ProductID = models.ForeignKey('Products', on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=1)