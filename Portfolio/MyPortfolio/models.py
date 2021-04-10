from django.db import models

class Project(models.Model):

    project_name = models.CharField(max_length = 50)
    description = models.TextField()
    image = models.ImageField(upload_to="images")
    tech_used = models.CharField(max_length = 20)
    code_link = models.CharField(max_length = 1000, default = 'https://codepen.io')

    def __str__(self):
        return self.project_name