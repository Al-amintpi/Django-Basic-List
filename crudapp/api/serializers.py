from rest_framework import serializers
from crudapp.models import Person 

class PersonSerializers(serializers.ModelSerializer):
	class Meta:
		model  = Person

		fields = (
			'id',
			'name',
			'email',
			'location',
			)