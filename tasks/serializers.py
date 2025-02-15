from rest_framework import serializers
from .models import Task, Tag
import datetime
from datetime import date



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('id','create_date','update_date', 'archived')

    def update(self, instance, validated_data):
        validated_data['update_date'] = datetime.datetime.now()
        return super().update(instance, validated_data)

    def validate_name(self, value):
        special_characters = '"\'!@#$%^&*()-+?_=,<>/'
        for char in value:
            if char in special_characters:
                raise serializers.ValidationError('Task name cannot contain special characters')
        return value.lower()


    def validate_deadline_date(self, value):
        if date.today() > value:
            return serializers.ValidationError('Task deadline date must be after today')
        return value

    def validate_description(self, value):
        if len(value.split()) < 10:
            raise serializers.ValidationError('Task description must be at least 10 word')
        return value


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

    def validate_name(self, value):
        special_characters = '"\'!@  # $%^&*()-+?_=,<>/'
        for char in value:
            if char in special_characters:
                raise serializers.ValidationError('Tag name cannot contain special characters')
        return value.lower()
