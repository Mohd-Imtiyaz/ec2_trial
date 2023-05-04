from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class education(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    institue_name = models.CharField(max_length=100, null=True)
    degree = models.CharField(max_length=100, null=True, blank=True)
    feild_of_study = models.CharField(max_length=80, null=True, blank=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    grade = models.CharField(max_length=10, null=True, blank=True)
    activities_societies = models.TextField(max_length=500, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    
    def __str__(self):
        return self.user_name.username

class license_certification(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    issuing_organization = models.CharField(max_length=60, null=True)
    issue_date = models.DateField()
    expiry_date = models.DateField(blank=True)
    credential_id = models.CharField(max_length=40, null=True, blank=True)
    credential_url = models.URLField(max_length=300, null=True, blank=True)
    
    def __str__(self):
        return self.user_name.username

class Skill(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class skills_selection(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill,
        related_name='user_skills', 
    )
    
    def __str__(self):
        return self.user_name.username

class Project(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=50, null=True)
    working_on_the_project = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField(blank=True)
    description = models.TextField(max_length=2000, null=True)
    project_url = models.URLField(max_length=200, null=True, blank=True)
    
    
    def __str__(self):
        return self.user_name.username

class Profile(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(max_length=500, null=True, default="Describe about yourself.")
    industry = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=30, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    linkedin_url = models.URLField(max_length=100, null=True, blank=True)
    github_url = models.URLField(max_length=100, null=True, blank=True)
    website_url = models.URLField(max_length=100, null=True, blank=True)
    address = models.TextField(max_length=500, null=True, blank=True)
    birthday = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.user_name.username


themes = (
    ("dark", "dark"),
    ("light", "light"),
)
class Theme(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    color = models.CharField(choices=themes, default="light", max_length=30)

    def __str__(self):
        return self.user.username

class Company_profile(models.Model):
    company_name = models.CharField(max_length=200, null=True)
    about_company = models.TextField(max_length=200, null=True)
    company_location = models.TextField(max_length=500, null=True)
    website_url = models.URLField(max_length=300, null=True, blank=True)
    founded_on = models.DateField(null=True)
    company_size = models.IntegerField(null=True)
    specilities = models.CharField(max_length=500, null=True)
    active = models.BooleanField(default=True)
    group_name = models.OneToOneField(Group, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.company_name