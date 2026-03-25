from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class About(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to='images/')


class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tools = models.CharField(max_length=200)
    link = models.URLField()


class Education(models.Model):
    school = models.CharField(max_length=150)
    course = models.CharField(max_length=150)
    year = models.CharField(max_length=50)

    def __str__(self):
        return self.school


class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    facebook = models.CharField(max_length=100)

    def __str__(self):
        return self.email