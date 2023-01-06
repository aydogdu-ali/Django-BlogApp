
from rest_framework import serializers 

from.models import Category, Blog #oluşturduğum modelleri import ediyoruz.


#serializers tanımlıyorum.
class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category #modelimiz ile eşleştiriyoruz.
        fields = (
            'id',
            'name'
        )
        

class BlogSerializers(serializers.ModelSerializer):
    category = serializers.StringRelatedField() # categorinin ismini gösterir
    category_id = serializers.IntegerField(write_only=True) #sadcepostput ve patch işlemlerinde gösterilir. 

    class Meta:
        model = Blog ##modelimiz ile eşleştiriyoruz.
        fields = (
            'id',
            'title',
            'content',
            'category_id',
            'category',
            'is_published',
            'created_date',
        ) #fielsd de category ismi gösteririr.
