from django.contrib import admin
from django.forms.widgets import Textarea
from django.db import models
from django import forms

admin.site.site_header = "Portfolio Admin"

# Register your models here.
from .models import ResumeProject, ResumeProjectDetail, ToolsUsed, RelatedLinks


class ResumeProjectDetailInlineFrom(forms.ModelForm):
    class Meta:
        model = ResumeProjectDetail
        widgets = {"explanation": forms.Textarea}
        fields = "__all__"


class ResumeProjectDetailInline(admin.StackedInline):
    model = ResumeProjectDetail
    extra = 0
    form = ResumeProjectDetailInlineFrom


class ResumeProjectRelatedLinksInline(admin.StackedInline):
    model = RelatedLinks
    extra = 0


class ResumeProjectForm(forms.ModelForm):
    class Meta:
        model = ResumeProject
        widgets = {
            "quick_blurb": forms.Textarea,
        }
        fields = "__all__"


@admin.register(ResumeProject)
class ResumeProjectAdmin(admin.ModelAdmin):
    inlines = (
        ResumeProjectDetailInline,
        ResumeProjectRelatedLinksInline,
    )
    list_display = (
        "start_date",
        "ongoing",
        "name",
        "difficulty",
    )
    form = ResumeProjectForm


@admin.register(ToolsUsed)
class ToolsUsedAdmin(admin.ModelAdmin):
    list_displpay = (
        "tool_name",
        "tool_color",
    )


@admin.register(ResumeProjectDetail)
class ResumeProjectDetailAdmin(admin.ModelAdmin):
    list_display = ("get_related_project",)

    def get_related_project(self, obj: ResumeProjectDetail):
        return obj.associated_project.name

    get_related_project.short_description = "Project Name"  # type: ignore


@admin.register(RelatedLinks)
class RelatedLinksAdmin(admin.ModelAdmin):
    list_display = (
        "link_name",
        "link_url",
    )
