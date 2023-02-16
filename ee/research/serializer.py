from rest_framework import serializers
from .models import Research, Labs, Papers, Projects


class ResearchSerializers(serializers.ModelSerializer):
    class Meta:
        model = Research
        fields = '__all__'

    def create(self, validated_data):
        research = Research.objects.create(specialization=validated_data.get('specialization'),
                                           person=validated_data.get('person'),
                                           description=validated_data.get('description'))
        return research

    def update(self, validated_data):
        try:
            research = Research.objects.get(validated_data['research_id'])
        except research.DoesNotExist:
            raise ValueError('research with the following id does not exist')

        if validated_data.get('specialization'):
            research.specialization = validated_data.get('specialization')
        if validated_data.get('person'):
            research.person = validated_data.get('person')
        if validated_data.get('description'):
            research.description = validated_data.get('description')

        research.save(
            update_fields=['specialization', 'person', 'description'])
        return research


class LabsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labs
        fields = '__all__'

    def create(self, validated_data):
        labs = Labs.objects.create(name=validated_data.get('name'),
                                   person=validated_data.get('person'),
                                   link=validated_data.get('link'))
        return labs

    def update(self, validated_data):
        try:
            labs = Labs.objects.get(id=validated_data['labs_id'])
        except labs.DoesNotExist:
            raise ValueError('lab with the required id does not exist')
        
        if validated_data.get('name'):
            labs.name = validated_data.get('name')
        if validated_data.get('link'):
            labs.link = validated_data.get('link')
        if validated_data.get('person'):
            labs.person = validated_data.get('person')
        labs.save(update_fields=['name', 'person', 'link'])


class PapersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Papers
        fields = '__all__'

    def create(self, validated_data):
        Paper = Papers.objects.create(specialization=validated_data.get('specialization'),
                                           person=validated_data.get('person'),
                                           description=validated_data.get('description'))
        return Paper

    def update(self, validated_data):
        try:
            Paper = Papers.objects.get(validated_data['Papers_id'])
        except Paper.DoesNotExist:
            raise ValueError('Papers with the following id does not exist')

        if validated_data.get('specialization'):
            Paper.specialization = validated_data.get('specialization')
        if validated_data.get('person'):
            Paper.person = validated_data.get('person')
        if validated_data.get('description'):
            Paper.description = validated_data.get('description')

        Paper.save(
            update_fields=['specialization', 'person', 'description'])
        return Paper


class ProjectsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

    def create(self, validated_data):
        Project = Projects.objects.create(specialization=validated_data.get('specialization'),
                                           person=validated_data.get('person'),
                                           description=validated_data.get('description'))
        return Project

    def update(self, validated_data):
        try:
            Project = Projects.objects.get(validated_data['Projects_id'])
        except Project.DoesNotExist:
            raise ValueError('Projects with the following id does not exist')

        if validated_data.get('specialization'):
            Project.specialization = validated_data.get('specialization')
        if validated_data.get('person'):
            Project.person = validated_data.get('person')
        if validated_data.get('description'):
            Project.description = validated_data.get('description')

        Project.save(
            update_fields=['specialization', 'person', 'description'])
        return Project
