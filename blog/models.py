from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=25, unique=True) #Aynı kategoriden 1 den fazla olamaz.

    def __str__(self): #tabloda ismi gözükmesi için yazdım.
        return self.name




class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete= models.PROTECT) #foreingkey onetomany ilişki demektir. Yani blogdaki yazılar aynı categoriye sahip olabilir demektir.
    #BURDA CATEGORY SİLİNİRSE BLOG SİLİNMESİN KORU ANLAMINDADIR.
    is_published = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self): # #tabloda ismi gözükmesi için yazdım.
        return self.title