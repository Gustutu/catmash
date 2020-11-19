from rest_framework import serializers
from django.db import models


class Cat(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    image = models.BinaryField()
    score = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cats'


class CatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cat
        fields = ('id', 'image', 'score')
