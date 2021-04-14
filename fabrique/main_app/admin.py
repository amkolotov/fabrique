from django.contrib import admin

from .models import Survey, Question, Response


class QuestionInline(admin.TabularInline):
    """Администрирование вопросов"""
    model = Question
    extra = 1


@admin.register(Survey)
class Survey(admin.ModelAdmin):
    """Администрирование опросов"""
    list_display = ('title', 'start_date', 'finish_date', 'text', 'is_active')
    list_display_links = ('title', 'start_date', 'is_active')
    inlines = [QuestionInline]
    readonly_fields = ('start_date',)
    save_on_top = True


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    """Администрирование ответов"""
    list_display = ('ip', 'question', 'choice_text', 'pub_date')
    list_display_links = ('question',)
    readonly_fields = ('ip', 'question', 'choice_text', 'pub_date')

