from celery import shared_task

@shared_task
def notify_donations(project_title, donor_name, amount):
    message = f"New donation received:\nProject: {project_title}\nDonor: {donor_name}\nAmount: {amount}"
    print(message)


