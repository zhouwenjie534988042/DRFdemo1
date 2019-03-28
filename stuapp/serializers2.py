from rest_framework import serializers

from stuapp.models import Actor


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        # fields = '__all__'
        fields = ('aid','aname','age','agender')
        read_only_fields = ('aid',)
        extra_kwargs = {
            'age': {'min_value': 0, 'required': False},
            'agender': {'required': False}
        }

