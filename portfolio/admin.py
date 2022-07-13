
from django.contrib import admin

# Register your models here.

from .models import About, Category, Home, Portfolio, Profile, Skill

# Home
admin.site.register(Home)

# About
class ProfileInLine(admin.TabularInline):
    model = Profile
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInLine,
    ]

# Skills
class SkillsInLine(admin.TabularInline):
    model = Skill
    extra: 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        SkillsInLine,
    ]

# Portfolio
admin.site.register(Portfolio)