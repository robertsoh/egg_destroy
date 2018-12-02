from django.contrib import admin
from apps.scores.models import Score


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):

    list_display = ('id', 'username', 'score_ms')
    search_fields = ('username',)
