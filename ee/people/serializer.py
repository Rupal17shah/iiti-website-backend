from rest_framework import serializers
from .models import People


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = '__all__'

    def create(self, validated_data):
        people = People.objects.create(people_cat=validated_data.get('people_cat'),
                                       name=validated_data.get('name'),
                                       title=validated_data.get('title'),
                                       email=validated_data.get('email'),
                                       details=validated_data.get('details'),
                                       link=validated_data.get('link'),
                                       address=validated_data.get('address'),
                                       subject=validated_data.get('subject'))
        return people

    def update(self, validated_data):
        try:
            people = People.objects.get(validated_data['people_id'])
        except people.DoesNotExist:
            raise ValueError('people of the given ID does not exist')
        if validated_data.get('people_cat'):
            people.people_cat = validated_data.get('people_cat')
        if validated_data.get('name'):
            people.name = validated_data.get('name')
        if validated_data.get('title'):
            people.title = validated_data.get('title')
        if validated_data.get('email'):
            people.email = validated_data.get('email')
        if validated_data.get('details'):
            people.details = validated_data.get('details')
        if validated_data.get('link'):
            people.link = validated_data.get('link')
        if validated_data.get('address'):
            people.address = validated_data.get('address')
        if validated_data.get('subject'):
            people.subject = validated_data.get('subject')

        people.save(update_fields=['people_type', 'people_cat', 'name',
                    'title', 'email', 'details', 'link', 'address', 'subject'])
        return people
