from django.db import models

# Create your models here.
from cloudinary.models import CloudinaryField


class ResumeProject(models.Model):

    start_date = models.DateField(("Start Date"), auto_now=False, auto_now_add=False)
    ongoing = models.BooleanField(("Ongoing"))
    name = models.CharField(("Title"), max_length=50, null=False, blank=False)
    quick_blurb = models.CharField(
        ("Quick Blurb"), max_length=200, null=False, blank=False
    )
    long_description = models.TextField(("Long Description"), blank=True)
    git_link = models.CharField(("Git Link"), max_length=200, blank=True)
    # main_img = models.ImageField(("Image Upload"), upload_to="resume/")
    main_img = CloudinaryField("Image Upload")
    difficulty = models.IntegerField(("Difficulty"), default=0)
    tools_used = models.ManyToManyField("resume.ToolsUsed", verbose_name=("Tools Used"))

    class Meta:
        verbose_name = "ResumeProject"
        verbose_name_plural = "ResumeProjects"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ResumeProject_detail", kwargs={"pk": self.pk})


class ResumeProjectDetail(models.Model):

    associated_project = models.ForeignKey(ResumeProject, on_delete=models.CASCADE)
    detail_short = models.CharField(("Short Detail"), max_length=100)
    explanation = models.CharField(("Longer Explanation"), max_length=250)

    class Meta:
        verbose_name = "ResumeProjectDetail"
        verbose_name_plural = "ResumeProjectDetails"

    def __str__(self):
        return "{} - {}".format(self.associated_project.name, self.detail_short)

    def get_absolute_url(self):
        return reverse("ResumeProjectDetail_detail", kwargs={"pk": self.pk})


class ToolsUsed(models.Model):
    tool_name = models.CharField(("Tool Name"), max_length=50)
    tool_color = models.CharField(("Tool Color"), max_length=50)

    def __str__(self):
        return self.tool_name


class RelatedLinks(models.Model):
    related_project = models.ForeignKey(
        "resume.ResumeProject", on_delete=models.CASCADE
    )
    link_name = models.CharField(("Link Name"), max_length=50)
    link_url = models.CharField(("Link"), max_length=250)

    def __str__(self):
        pass

    class Meta:
        verbose_name = "RelatedLinks"
        verbose_name_plural = "RelatedLinkss"
