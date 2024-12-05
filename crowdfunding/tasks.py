from datetime import datetime

from celery import shared_task

from .models import Project

@shared_task
def notify_donations(project_title, donor_name, amount):
    message = f"New donation received:\nProject: {project_title}\nDonor: {donor_name}\nAmount: {amount}"
    print(message)

@shared_task
def check_project_deadline():

    now = datetime.now()

    expired_projects = Project.status_projects.get_open_projects.filter(deadline__lt=now)

    for project in expired_projects:
        project.status = Project.ProjectStatus.FAILED
        project.save()


