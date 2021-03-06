from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import  Cat, CatSerializer
from django.shortcuts import get_object_or_404
import random
from rest_framework.response import Response
import json
from . import computeElo
# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class CatViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing accounts.
    """
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class Cutest(viewsets.ViewSet):
    """
    Enpoint to post cutest cats of two presented to user
    """

    def create(self, request, format=None):
        """
        Return a list of all users.
        """
        parsed_body = json.loads(request.body)
        print(request.body)
        cat1_id = parsed_body["catsIds"][0]
        cat2_id = parsed_body["catsIds"][1]
        winner_id = parsed_body["winnerId"]

        cat1 = Cat.objects.get(id=cat1_id)
        cat2 = Cat.objects.get(id=cat2_id)

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




