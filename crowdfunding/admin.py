from django.contrib import admin

from .models import Project, Donation

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'goal_amount', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'description')


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('project', 'donor_name', 'amount', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('donor_name',)
