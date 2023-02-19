from rest_framework import authentication, generics, mixins, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.http import Http404
from django.shortcuts import get_object_or_404

# from api.authentication import TokenAuthentication
from api.mixins import StaffEditorPermissionMixin

from .models import Product
# from api.permissions import IsStaffEditorPermission
from .serializers import ProductSerializer


# Create your views here.

class ProductListCreateAPIView(StaffEditorPermissionMixin, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    ##########----- NOT NEEDED AFTER ADDING THE DEFAULT AUTH IN SETTING ----########
    # authentication_classes = [
    #     authentication.SessionAuthentication,
    #     # authentication.TokenAuthentication,
    #     TokenAuthentication,
    # ]
    ###--------- NOT NEEDED ANY MORE AFTER CREATING PERMISSION MIXINS
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # email = serializer.validated_data.pop('email')
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        print(serializer)
        serializer.save(content=content) # similar to form.save() and model.save()
        #can send a django signal here

product_list_create_view = ProductListCreateAPIView.as_view()


class ProductDetailAPIView(StaffEditorPermissionMixin, generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'

product_detail_view = ProductDetailAPIView.as_view()


class ProductUpdateAPIView(StaffEditorPermissionMixin, generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            ##

product_update_view = ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(StaffEditorPermissionMixin, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        #instance
        super().perform_destroy(instance)

product_destroy_view = ProductDestroyAPIView.as_view()


class ProductListAPIView(generics.ListAPIView):
    """
    Not going to use this method
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'

product_list_view = ProductListAPIView.as_view()


class ProductMixinView(mixins.ListModelMixin, 
                        mixins.RetrieveModelMixin,
                        mixins.CreateModelMixin, 
                        generics.GenericAPIView
                    ):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
     
    def get(self, request, *args, **kwargs): #HTTP -> GET
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, )
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs): #HTTP -> post
       return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = "This is a single view doing cool stuff!!!"
        print(serializer)
        serializer.save(content=content)

product_mixin_view = ProductMixinView.as_view()


@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    if method == "GET":
        if pk is not None:
            #detail view
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data      
            return Response(data)
        #list view
        qs = Product.objects.all()
        data = ProductSerializer(qs, many=True).data
        return Response(data)

    if method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get(title)
            content = serializer.validated_data.get(content) or None
            if content is None:
                content = title
            serializer.save(content=content)
        return Response(data)
    return Response({'Invalid': "not good data"}, status=400)

    
