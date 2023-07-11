from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):

	class Meta:
		model = Book
		fields = "__all__"

	def create(self, data):
		return Book.objects.create(**data)