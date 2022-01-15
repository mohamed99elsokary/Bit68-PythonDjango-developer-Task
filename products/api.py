from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import models, serializers


@api_view(["POST", "PUT", "GET", "DELETE"])
def products(request):
    if request.method == "POST":
        serializer = serializers.CreateProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "GET":

        seller = request.GET.get("seller")
        order = request.GET.get("order")
        if seller:
            try:
                seller = Token.objects.get(key=seller)
            except:
                return Response(
                    {"seller": ["Invalid Token."]}, status=status.HTTP_400_BAD_REQUEST
                )
            if order == "descending":
                products = models.Product.objects.filter(seller=seller.user).order_by(
                    "-price"
                )
            elif order == "ascending":
                products = models.Product.objects.filter(seller=seller.user).order_by(
                    "price"
                )
            else:
                products = models.Product.objects.filter(seller=seller.user)
        else:
            if order == "descending":
                products = (
                    models.Product.objects.all().order_by("seller").order_by("-price")
                )
            elif order == "ascending":
                products = (
                    models.Product.objects.all().order_by("seller").order_by("price")
                )
            else:
                products = models.Product.objects.all().order_by("seller")

        serializer = serializers.ProductSerializer(products, many=True)
        return Response(serializer.data)
