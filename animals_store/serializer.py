from rest_framework import serializers
from .models import Species, Animals, Behavior
from django.conf import settings

class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = '__all__'

class AnimalsSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only=True, required=False)
    class Meta:
        model = Animals
        fields = '__all__'

    def create(self, validated_data):
        image = validated_data.pop('image', None)
        animals = super().create(validated_data)
        if image:
            animals.image_url = self.save_image(animals, image)
            animals.save()
        return animals

    def update(self, instance, validated_data):
        image = validated_data.pop('image', None)
        animals = super().update(instance, validated_data)
        if image:
            animals.image_url = self.save_image(animals, image)
            animals.save()
        return animals

    def save_image(self, animals, image):
        from django.core.files.storage import default_storage
        from django.core.files.base import ContentFile
        import os

        path =default_storage.save(os.path.join('images', str(animals.id) + '_' + image.name), ContentFile(image.read()))
        return settings.MEDIA_URL +  path

class BehaviorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Behavior
        fields = '__all__'