from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.name
class Info(models.Model):
    name = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    summary = models.TextField()
    work_experience = models.TextField()
    skills = models.TextField()
    education = models.TextField()

    def __str__(self):
        return self.name
