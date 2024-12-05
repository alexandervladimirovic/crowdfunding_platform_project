from rest_framework import serializers

from .models import Project, Donation

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'goal_amount', 'status', 'created_at', 'updated_at']


class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ['id', 'project', 'donor_name', 'amount', 'created_at']