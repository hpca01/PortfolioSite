from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import ResumeProject, ResumeProjectDetail

# Create your views here.
def home(request):
    return render(request, "home.html")


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


def hobbies(request):
    return render(request, "hobbies.html")


class ProjectListView(ListView):
    model = ResumeProject
    context_object_name = "projects"
    template_name = "projects_list.html"

    def get_queryset(self):
        return ResumeProject.objects.all().order_by("-difficulty", "start_date")


class ProjectDetailView(DetailView):
    model = ResumeProject
    context_object_name = "project"
    template_name = "project_detail.html"

    def get_queryset(self):
        return (
            ResumeProject.objects.filter(pk=self.kwargs["pk"])
            .select_related()
            .prefetch_related()
        )
