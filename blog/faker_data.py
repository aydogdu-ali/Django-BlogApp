

from faker import Faker
from .models import Category, Blog

def run():
    fake =Faker(['tr-TR'])
    categories = ('Yaşam', 'Bilim','Sanat','Spor')

    for category in categories:
        new_category = Category.objects.create(name=category)
        for i in range(10):
            Blog.objects.create(category=new_category,title = fake.name(), content=fake.text())
    print("finished")