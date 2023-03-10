import json
from django.forms.models import model_to_dict 
# from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer


# Create your views here.
@api_view(['POST']) #convert a function based view into an API VIEW
def api_home(request, *args, **kwargs) -> Response:
    # data = request.data
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        # print('instance: ', instance)
        print('serializer.data: ', serializer.data)
        data = serializer.data
        return Response(data)
    return Response({'Invalid': "not good data"}, status=400)




"""
@api_view(['GET']) #convert a function based view into an API VIEW
def api_home(request, *args, **kwargs) -> Response:
    instance = Product.objects.all().order_by("?").first()
    data = {}
    print(instance)
    if instance:
        # data = model_to_dict(instance,  fields=['id', 'title'])
        data = ProductSerializer(instance).data
        print(data)
    return Response(data)
"""

#Initial api_home
"""
@api_view(['GET']) #convert a function based view into an API VIEW
def api_home(request, *args, **kwargs) -> Response:
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data,  fields=['id', 'title'])
    return Response(data)
    
def api_home(request, *args, **kwargs) -> JsonResponse:
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    print(request.GET)
    if model_data:
        data = model_to_dict(model_data,  fields=['id', 'title'])
    return JsonResponse(data)


def api_home(request, *args, **kwargs) -> HttpResponse:
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    print(request.GET)
    if model_data:
        # model instance (model_data)
        # turn to a python dict
        # return JSON to my client
        # serialization
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
        data = model_to_dict(model_data,  fields=['id', 'title'])
        json_data_str = json.dumps(data)
    return HttpResponse(json_data_str, headers={"content-type": "application/json"})

def api_home(request, *args, **kwargs) -> JsonResponse:
    # request -> HttpRequest -> Django
    # print(dir(request))
    # request.body
    print(request.GET) #URL QUERY PARAMETERS
    body = request.body #byte string of JSON data
    data = {}
    try:
        data = json.loads(body) #takes in a string of JSON DATA -> Python Dictionary
    except Exception as e:
        pass
    print(data)
    print(dict(request.headers))
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)
"""