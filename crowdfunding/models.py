from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

MIN_GOAL_AMOUNT = 100000
MIN_DONATION_AMOUNT = 1000

class StatusProjectManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Project.ProjectStatus.OPEN)
    
    def get_open_projects(self):
        return self.get_queryset()
    
    def get_closed_projects(self):
        return super().get_queryset().filter(status=Project.ProjectStatus.CLOSED)
    
    def get_failed_projects(self):
        return super().get_queryset().filter(status=Project.ProjectStatus.FAILED)

class Project(models.Model):

    class ProjectStatus(models.TextChoices):

        OPEN = 'open', _('Open')
        CLOSED = 'closed', _('Closed')
        FAILED = 'failed', _('Failed')

    title = models.CharField(_("title of the project"), max_length=200)
    description = models.TextField(_("description of the project"))
    goal_amount = models.DecimalField(_("goal amount"), max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)
    status = models.CharField(_('status'), max_length=10, choices=ProjectStatus.choices, default=ProjectStatus.OPEN)

    objects = models.Manager()
    status_projects = StatusProjectManager()
    
    class Meta:
        verbose_name = _("project")
        verbose_name_plural = _("projects")
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['status'])
        ]

    def __str__(self):
        return self.title
    
    def clean(self):
        if self.goal_amount < MIN_GOAL_AMOUNT:
            raise ValidationError(_("Goal amount must be greater than 100000"))
        
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

class Donation(models.Model):

    project = models.ForeignKey(Project, verbose_name=_("project"), on_delete=models.CASCADE, related_name='donations')
    donor_name = models.CharField(_("donor name"), max_length=100)
    amount = models.DecimalField(_("amount"), max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)

    class Meta:
        verbose_name = _("donation")
        verbose_name_plural = _("donations")
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at'])
        ]
    
    def __str__(self):
        return f"{self.donor_name} - {self.amount} for {self.project.title}"
    
    def clean(self):
        if self.amount < MIN_DONATION_AMOUNT:
            raise ValidationError(_("Donation amount must be greater than 1000"))
        
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)