from django.contrib import admin

from adminsortable.admin import (SortableAdmin, SortableTabularInline,
    SortableStackedInline, SortableGenericStackedInline, SortableInlinesAdmin)
from app.models import Category, Project, Agenda, Credit, Note, GenericNote


admin.site.register(Category, SortableAdmin)


class CreditInline(SortableTabularInline):
    model = Credit


class NoteInline(SortableStackedInline):
    model = Note
    extra = 0


class GenericNoteInline(SortableGenericStackedInline):
    model = GenericNote
    extra = 0


class ProjectAdmin(SortableAdmin):
    inlines = [CreditInline, NoteInline, GenericNoteInline]
    list_display = ['__unicode__', 'category']

admin.site.register(Project, ProjectAdmin)


class AgendaAdmin(SortableInlinesAdmin):
    inlines = [GenericNoteInline]
    list_display = ['__unicode__']

admin.site.register(Agenda, AgendaAdmin)
