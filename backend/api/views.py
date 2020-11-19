from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Cat, CatSerializer
from django.shortcuts import get_object_or_404
import random
from rest_framework.response import Response

# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class CatView(viewsets.ViewSet):
    """
    API endpoint to get two different  random cats
    """
        
    def list(self, request):
        queryset = Cat.objects.all()
        # cats = []
        # TODO: move to dja,go init
        my_ids = Cat.objects.values_list('id', flat=True)
        my_ids = list(my_ids)
        rand_ids = random.sample(my_ids, 2)
        # cats.append(get_object_or_404(queryset, pk=pk))
        two_random_cat = Cat.objects.filter(id__in=rand_ids)

        serializer = CatSerializer(two_random_cat, many=True)
    
        return Response(serializer.data)
    

# TODO: move to django initialisation

        my_ids = Cat.objects.values_list('id', flat=True)
        my_ids = list(my_ids)
        n = 2
        rand_ids = random.sample(my_ids, n)
