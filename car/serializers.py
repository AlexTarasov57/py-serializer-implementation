from django.core.validators import MaxValueValidator, MinValueValidator
from rest_framework import serializers

from car.models import Car


# manufacturer = models.CharField(max_length=64)
# model = models.CharField(max_length=64)
# horse_powers = models.PositiveSmallIntegerField(
#     validators=[MaxValueValidator(1914), MinValueValidator(1)]
# )
# is_broken = models.BooleanField()
# problem_description = models.TextField(null=True, blank=True)


# def __str__(self):
#     return f"{self.manufacturer}, {self.model}"
class CarSerializer(serializers.Serializer):
    manufacturer = serializers.CharField(max_length=64)
    model = serializers.CharField(max_length=64)
    horse_powers = serializers.PositiveSmallIntegerField(
        min_value=1,
        max_value=1914
)
    is_broken = serializers.BooleanField()
    problem_description = serializers.CharField(required=False, allow_blank=True)

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.manufacturer = validated_data.get('manufacturer', instance.manufacturer)
        instance.model = validated_data.get('model', instance.model)
        instance.horse_powers = validated_data.get('horse_powers', instance.horse_powers)
        instance.is_broken = validated_data.get('is_broken', instance.is_broken)
        instance.problem_description = validated_data.get('problem_description', instance.problem_description)
        return instance

    class Meta:
        model = Car
        fields = "__all__"
