from django.db import models


class Mentor(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    github = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    skills = models.CharField(max_length=255)

    user = models.ForeignKey('user.CustomUser', on_delete=models.SET(1))
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} (Github@{self.github}, {self.location})"

    class Meta:
        db_table = 'mentors'
