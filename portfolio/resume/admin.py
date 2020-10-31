from django.contrib import admin

# Register your models here.
from .models import ResumeProject, ResumeProjectDetail, ToolsUsed


class ResumeProjectDetailInline(admin.StackedInline):
    model = ResumeProjectDetail
    extra = 0


@admin.register(ResumeProject)
class ResumeProjectAdmin(admin.ModelAdmin):
    inlines = (ResumeProjectDetailInline,)
    list_display = (
        "start_date",
        "ongoing",
        "name",
        "difficulty",
    )


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
