from rest_framework import serializers
from .models import Paper, Level, Subject

# Serializer for Level model
class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'

# Serializer for Subject model
class SubjectSerializer(serializers.ModelSerializer):
      class Meta:
            model = Subject
            fields = '__all__'

# Serializer for Paper model
class PaperSerializer(serializers.ModelSerializer):
      level = LevelSerializer(read_only=True)
      subject = SubjectSerializer(read_only=True)

      class Meta:
          model = Paper
          fields = '__all__'
          