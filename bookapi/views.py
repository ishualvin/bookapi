from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class BookView(APIView):


	def post(self, request, format=None):
		serializer = BookSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({
				'message' : 'Book Upload Successfully',
				'status' : 'success',
				'candidate' : serializer.data
				},status = status.HTTP_201_CREATED
			)
		return Response(serializer.errors)


	def get(self, request, pk=None, format=None):
		if pk is None:
			# Handle the case when pk is not provided
			# This can be used to retrieve a list of books instead of a specific book
			books = Book.objects.all()
			serializer = BookSerializer(books, many=True)
			return Response({
            	'status': 'success',
            	'books': serializer.data
        	}, status=status.HTTP_200_OK)
		else:
			# Handle the case when pk is provided
			try:
				book = Book.objects.get(pk=pk)
				serializer = BookSerializer(book)
				return Response({
                	'status': 'success',
                	'book': serializer.data
            	}, status=status.HTTP_200_OK)
			except Book.DoesNotExist:
				return Response({
                	'status': 'error',
                	'message': 'Book not found'
            	}, status=status.HTTP_404_NOT_FOUND)