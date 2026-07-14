from django.contrib import admin
from .models import Mission, PlayerSession, AnswerLog

@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ('title', 'phase', 'order', 'expected_answer', 'points', 'reward')
    list_editable = ('phase', 'order', 'points')
    list_filter = ('phase',)
    search_fields = ('title', 'story', 'question', 'expected_answer', 'reward')

class AnswerLogInline(admin.TabularInline):
    model = AnswerLog
    extra = 0
    readonly_fields = ('mission', 'answer', 'correct', 'created_at')

@admin.register(PlayerSession)
class PlayerSessionAdmin(admin.ModelAdmin):
    list_display = ('player_name', 'selected_phase', 'score', 'current_mission', 'finished', 'created_at')
    list_filter = ('selected_phase', 'finished')
    inlines = [AnswerLogInline]

@admin.register(AnswerLog)
class AnswerLogAdmin(admin.ModelAdmin):
    list_display = ('session', 'mission', 'answer', 'correct', 'created_at')
    list_filter = ('correct', 'mission__phase')
