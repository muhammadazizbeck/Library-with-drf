from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id','title','subtitle','content','author','isbn','price')

    def validate(self, data):
        title = data.get('title',None)
        isbn = data.get('isbn',None)
        queryset = Book.objects.filter(title=title,isbn=isbn)

        if self.instance:
            queryset = queryset.exclude(id=self.instance.id)
        
        if queryset.exists():
            raise serializers.ValidationError(
                {
                    'status':'error',
                    'message':'Bir kitobni qayta-qayta joylash mumkin emas'
                }
            )
        return data