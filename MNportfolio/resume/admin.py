from django.contrib import admin
from .models import (
    Skill,
    Education,
    Experience,
    Language,
    HardSkill,
    SoftSkill,
    SocialLink,
    Personal_info,
    Facts,
    Service,
    Testimonial,
    PortfolioProject,
    Massage
)


class SkillAdmin(admin.ModelAdmin):
    list_display = ["name", "value", "created_on"]
    list_filter = ["value"]
    search_fields = ["name"]


class EducationAdmin(admin.ModelAdmin):
    list_display = ["university_name", "start_date",
                    "end_date", "grade", "created_on"]


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ["job_title", "company_name",
                    "start_date", "end_date", "created_on"]


class LanguageAdmin(admin.ModelAdmin):
    list_display = ["name", "level", "created_on"]


class HardSkillAdmin(admin.ModelAdmin):
    list_display = ["name", "created_on"]


class HardSkillAdmin(admin.ModelAdmin):
    list_display = ["name", "created_on"]


class SoftSkillAdmin(admin.ModelAdmin):
    list_display = ["name", "created_on"]


class FactsAdmin(admin.ModelAdmin):
    list_display = ["happy_clients_count", "happy_clients_description",
                    "projects_count", "projects_description",
                    "awards_count", "awards_description",
                    "years_of_exreiance", "years_of_exreiance_description", "created_on"]


class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ["link_name", "link", "created_on"]


class ServicekAdmin(admin.ModelAdmin):
    list_display = ["service_name", "created_on"]


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["name", "job_position", "created_on"]


class PortfolioProjectAdmin(admin.ModelAdmin):
    list_display = ["project_name", "project_url",
                    "project_date", "created_on"]


# Register your models here.
admin.site.register(Skill, SkillAdmin)
admin.site.register(Personal_info)  # , Personal_infoAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(HardSkill, HardSkillAdmin)
admin.site.register(SoftSkill, SoftSkillAdmin)
admin.site.register(Facts, FactsAdmin)
admin.site.register(SocialLink, SocialLinkAdmin)
admin.site.register(Service, ServicekAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(PortfolioProject, PortfolioProjectAdmin)
admin.site.register(Massage)
