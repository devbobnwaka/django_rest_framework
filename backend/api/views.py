import json
from django.forms.models import model_to_dict 
from django.http import JsonResponse, HttpResponse

from products.models import Product


# Create your views here.
def api_home(request, *args, **kwargs) -> JsonResponse:
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    print(request.GET)
    if model_data:
        data = model_to_dict(model_data,  fields=['id', 'title'])
    return JsonResponse(data)

#Initial api_home
"""
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