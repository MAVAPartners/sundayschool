from rest_framework import serializers

from exam.models import Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['id','score','accademicYear','is_approved', 'status']

    def create(self, validated_data):
        return School.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.score = validated_data.get('score', instance.score)
        instance.accademicYear = validated_data.get('accademicYear', instance.accademicYear)
        instance.is_approved = validated_data.get('is_approved', instance.is_approved)
        instance.status = validated_data.get('status', instance.status)

        instance.save()
        return instance
