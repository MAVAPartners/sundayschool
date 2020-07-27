from rest_framework import serializers

from exam.models import School


class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = ['name','description','is_active']

    def create(self, validated_data):
        return School.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.is_active = validated_data.get('is_active', instance.is_active)

        instance.save()
        return instance
