from rest_framework import serializers
from django.db import models

# le model Cat existe pour conserver les images en base de données et 
# délégué la gestion de la table a Django


class Cat(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    image = models.BinaryField()
    score = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cats'


class CatNoImage(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    score = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'cats'


class CatNoImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CatNoImage
        fields = ('id', 'score')


class CatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cat
        fields = ('id', 'image', 'score')
