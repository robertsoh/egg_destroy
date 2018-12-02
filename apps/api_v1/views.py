from rest_framework.generics import ListCreateAPIView

from apps.api_v1.serializers import ScoreSerializer
from apps.scores.models import Score


class ScoreCreateListAPIVIEW(ListCreateAPIView):
    serializer_class = ScoreSerializer

    def get_queryset(self):
        return Score.objects.order_by('-score_ms')[:1]

