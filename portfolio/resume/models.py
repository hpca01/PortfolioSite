from django.db import models

# Create your models here.

class ResumeProject(models.Model):

    start_date = models.DateField(("Start Date"), auto_now=False, auto_now_add=False)
    ongoing = models.BooleanField(("Ongoing"))
    quick_blurb = models.CharField(("Quick Blurb"), max_length=200, null=False, blank=False)
    long_description = models.TextField(("Long Description"), blank=True)
    git_link = models.CharField(("Git Link"), max_length=200)
    main_img = models.ImageField(("Image Upload"), upload_to='resume')


    class Meta:
        verbose_name = ("ResumeProject")
        verbose_name_plural = ("ResumeProjects")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ResumeProject_detail", kwargs={"pk": self.pk})

class ResumeProjectDetail(models.Model):

    associated_project = models.ForeignKey(ResumeProject, on_delete=models.CASCADE)
    detail_short = models.CharField(("Short Detail"), max_length=100)
    explanation = models.CharField(("Longer Explanation"), max_length=250)

    class Meta:
        verbose_name = ("ResumeProjectDetail")
        verbose_name_plural = ("ResumeProjectDetails")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ResumeProjectDetail_detail", kwargs={"pk": self.pk})
