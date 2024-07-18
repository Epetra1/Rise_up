from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category
from .serializers import CategorySerializer

class CategoryAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        category = Category.objects.create(
            category_title=data['category_title']
        )
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
