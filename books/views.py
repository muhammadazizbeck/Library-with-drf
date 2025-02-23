from django.shortcuts import render,get_object_or_404
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response



# Create your views here.

# class BookListApiView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class BookListCreateApiView(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookListApiView(APIView):
    def get(self,request):
        books = Book.objects.all()
        serializer = BookSerializer(books,many=True)
        context = {
            'data':serializer.data,
            'status':'Successfully',
            'message':'You took all of the books'
        }
        return Response(context)
    
class BookCreateApiView(APIView):
    def post(self,request):
        serializer = BookSerializer(data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            context = {
                'status':'success',
                'message':'Book is successfully created',
                'data':serializer.data
            }
            return Response(context,status=status.HTTP_201_CREATED)
        context = {
            'status':'error',
            'message':'Book was failed to create new one',
            'errors':serializer.errors
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)

class BookDetailApiView(APIView):
    def get(self,request,pk):
        try:
            book = get_object_or_404(Book,pk=pk)
            serializer = BookSerializer(book)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"},status=status.HTTP_404_NOT_FOUND)

# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class BookDeleteApiView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDeleteApiView(APIView):
    def delete(self,request,pk):
        try:
            book = get_object_or_404(Book,pk=pk)
            book.delete()
            context = {
                'status':'success',
                'message':'Book was successfully deleted'
            }
            return Response(context,status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist:
            context = {
                'error':'Book not found'
            }
            return Response(context,status=status.HTTP_404_NOT_FOUND)
        
class BookUpdateApiView(APIView):
    def put(self,request,pk):
        book = get_object_or_404(Book,pk=pk)
        serializer = BookSerializer(book,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            context = {
                'status':'success',
                'message':'Book was successfully updated',
                'data':serializer.data
            }
            return Response(context,status=status.HTTP_201_CREATED)
        context = {
            'status':'error',
            'message':'Something wrong here',
            'errors':serializer.errors
        }
        return Response(context,status=status.HTTP_404_NOT_FOUND)
    

# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class BookRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

