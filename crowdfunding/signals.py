from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Project, Donation
from .tasks import notify_donations

@receiver(post_save, sender=Donation)
def update_project_status(sender, instance, **kwargs):
    
    project = instance.project

    if project.total_donations() >= project.goal_amount:
        project.status = Project.ProjectStatus.CLOSED
        
    elif project.status == Project.ProjectStatus.OPEN and project.total_donations() < project.goal_amount:
        project.status = Project.ProjectStatus.OPEN
        
    project.save()

    notify_donations.delay(project.title, instance.donor_name, instance.amount)

