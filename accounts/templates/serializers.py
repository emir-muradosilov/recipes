from rest_framework import serializers
from recipe.models import Recept


class ReceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recept
        fields = ['author', 'recept_name', 'description', 'recept_text', 'img', 'is_published', 'category']

# ViewSets define the view behavior.

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Recept
        fields = ['title', 'id']
