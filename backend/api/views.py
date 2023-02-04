import json
from django.http import JsonResponse


# Create your views here.
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