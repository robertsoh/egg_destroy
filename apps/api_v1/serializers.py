from rest_framework import serializers

from apps.scores.models import Score


class ScoreSerializer(serializers.ModelSerializer):


    class Meta:
        model = Score
        fields = ('username', 'score_ms')
