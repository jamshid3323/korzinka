from django.shortcuts import render
from .models import ProductModel, CategoryModel
from rest_framework import views, generics, viewsets
from .serializers import ProductModelSerializers, CategoryModelSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryModelSerializers


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializers
# class ProductViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = ProductModel.objects.all()
#         serializer = ProductModelSerializers(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = get_object_or_404(ProductModel, pk=pk)
#         serializer = ProductModelSerializers(queryset)
#         return Response(serializer.data)
#
#     @action(methods=['get'], detail=True, url_path='cats')
#     def categories(self, request, pk=None):
#         if pk:
#             queryset = CategoryModel.objects.get(pk=pk)
#             serializer = CategoryModelSerializers(queryset)
#             return Response(serializer.data)
#         queryset = CategoryModel.objects.all()
#         serializer = CategoryModelSerializers(queryset, many=True)
#         return Response(serializer.data)

# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = ProductModel.objects.all()
#     serializer_class = ProductModelSerializers
#
#     @action(methods=['get'], url_path='cat', detail=False)
#     def category(self, request, pk=None):
#         if not pk:
#             cats = CategoryModel.objects.all()
#             serializer = CategoryModelSerializers(cats, many=True)
#             return Response(serializer.data)
#         cat = CategoryModel.objects.get(pk=pk)
#         serializer = CategoryModelSerializers(cat)
#         return Response(serializer.data)

# class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = ProductModel.objects.all()
#     serializer_class = ProductModelSerializers
#
#
# class ProductCreateView(generics.CreateAPIView):
#     serializer_class = ProductModelSerializers
#
#
# class ProductListView(generics.ListAPIView):
#     queryset = ProductModel.objects.all()
#     serializer_class = ProductModelSerializers
#
#
# class ProductModelView(views.APIView):
#
#     def get(self, request, pk=None, *args, **kwargs):
#         if pk:
#             instance = ProductModel.objects.get(pk=pk)
#             serializer = ProductModelSerializers(instance)
#         else:
#             instance = ProductModel.objects.all()
#             serializer = ProductModelSerializers(instance, many=True)
#
#         return Response(serializer.data)
#
#     def post(self, request, *args, **kwargs):
#         serializer = ProductModelSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
#     def patch(self, request, pk, *args, **kwargs):
#         instance = ProductModel.objects.get(pk=pk)
#         serializer = ProductModelSerializers(instance, partial=True, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, pk, *args, **kwargs):
#         instance = ProductModel.objects.get(pk=pk)
#         serializer = ProductModelSerializers(instance, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         instance = ProductModel.objects.get(pk=pk)
#         instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
