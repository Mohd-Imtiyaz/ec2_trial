from django.contrib import admin
from administration import models
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import GroupAdmin, UserAdmin
# Register your models here.
admin.site.register(models.license_certification)
admin.site.register(models.skills_selection)
admin.site.register(models.Project)
admin.site.register(models.education)
admin.site.unregister(Group)
admin.site.unregister(User)

################################### Skill CSV IMPORT AND EXPORT ######################################

class SkillResource(resources.ModelResource):
    user_name = fields.Field(
            column_name='user_name',
            attribute='user_name',
            widget=ForeignKeyWidget(User, 'username'))

        
    class Meta:
        model = models.Skill
        fields = ('id','name', 'abbreviation',)

class SkillAdmin(ImportExportModelAdmin):
    resource_class = SkillResource

admin.site.register(models.Skill, SkillAdmin)

################################### Profile CSV IMPORT AND EXPORT ######################################

class ProfileResource(resources.ModelResource):
    user_name = fields.Field(
            column_name='user_name',
            attribute='user_name',
            widget=ForeignKeyWidget(User, 'username'))
        
    class Meta:
        model = models.Profile
        fields = ('id','user_name','about','industry','country','city','linkedin_url','github_url','website_url','address','birthday',)

class ProfileAdmin(ImportExportModelAdmin):
    resource_class = ProfileResource
    list_display = ('user_name','birthday',)
    list_filter = ('user_name','country','city')

admin.site.register(models.Profile, ProfileAdmin)

class GroupAdminWithCount(GroupAdmin, ImportExportModelAdmin):
    def user_count(self, obj):
        return obj.user_set.count()

    list_display = GroupAdmin.list_display + ('user_count',)
    
admin.site.register(Group, GroupAdminWithCount)

class UserList(UserAdmin, ImportExportModelAdmin):
    list_display = ('username','email','is_active','date_joined')
    list_filter = ('username','is_superuser','is_staff','is_active','email','date_joined','groups')

admin.site.register(User, UserList)

class ThemeList(ImportExportModelAdmin):
    list_display = ('user','color',)
    list_filter = ('user','color',)

admin.site.register(models.Theme, ThemeList)

class CompanyList(admin.ModelAdmin):
    list_display = ('company_name','group_name','active','founded_on','company_location',)
    list_filter = ('company_name','active','founded_on','company_location',)

admin.site.register(models.Company_profile, CompanyList)