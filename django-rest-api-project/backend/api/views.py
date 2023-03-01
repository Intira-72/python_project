from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

@api_view(["GET", "POST"])
def api_home(request, *args, **kwargs):

    if request.method == "POST":
        return Response({"detail": "GET not allowed"}, status=405)
    else:
        instance = Product.objects.all().order_by("?").first()

        data = {}

        if instance:
            data = ProductSerializer(instance).data
            # data = model_to_dict(instance, fields=['id', 'title', 'price', 'sale_price'])

        return Response(data)