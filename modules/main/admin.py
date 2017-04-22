# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Employee, Skill, Organization, Experience, Project


class SkillsInline(admin.StackedInline):
    model = Skill


class ExperienceInLine(admin.StackedInline):
    model = Experience


class ProjectInLine(admin.StackedInline):
    model = Project


class EmplyeeAdmin(admin.ModelAdmin):
    inlines = [SkillsInline, ExperienceInLine, ProjectInLine]

    class Meta:
        model = Employee


class OrganizationeAdmin(admin.ModelAdmin):
    class Meta:
        model = Organization


admin.site.register(Employee, EmplyeeAdmin)
admin.site.register(Organization, OrganizationeAdmin)
