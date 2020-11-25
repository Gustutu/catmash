from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Cat, CatNoImage, CatNoImageSerializer, CatSerializer
from django.shortcuts import get_object_or_404
import random
from rest_framework.response import Response
import json
from . import computeElo
# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class CatView(viewsets.ViewSet):
    """
    API endpoint to get two different  random cats
    """
    
    def list(self, request):
        queryset = CatNoImage.objects.all()
        all_cats = CatNoImage.objects.all()
        serializer = CatNoImageSerializer(all_cats, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = CatNoImage.objects.all()
        # cats = []
        # TODO: move to dja,go init
        my_ids = CatNoImage.objects.values_list('id', flat=True)
        my_ids = list(my_ids)
        rand_ids = random.sample(my_ids, 2)
        # cats.append(get_object_or_404(queryset, pk=pk))
        two_random_cat = CatNoImage.objects.filter(id__in=rand_ids)

        serializer = CatNoImageSerializer(two_random_cat, many=True)

        return Response(serializer.data)

    def create(self, request):
        
        parsed_body = json.loads(request.body)
        print(request.body)
        cat1_id = parsed_body["catsIds"][0]
        cat2_id = parsed_body["catsIds"][1]
        winner_id = parsed_body["winnerId"]

        cat1 = CatNoImage.objects.get(id=cat1_id)
        cat2 = CatNoImage.objects.get(id=cat2_id)

        if cat1.id == winner_id:
            winner_cat = cat1
            looser_cat = cat2
        elif cat2.id == winner_id:
            winner_cat = cat2
            looser_cat = cat1
        else:
            # TODO: error response code
            print("winner not in cat Ids")

        winner_score, looser_score = computeElo.compute_new_scores(
            winner_cat.score, looser_cat.score)

        winner_cat.score = winner_score
        looser_cat.score = looser_score

        winner_cat.save()
        looser_cat.save()

        return Response()
