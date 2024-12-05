from rest_framework import serializers

from .models import Project, Donation

class ProjectSerializer(serializers.ModelSerializer):
    
    total_donations = serializers.SerializerMethodField()
    
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'goal_amount', 'total_donations', 'status', 'created_at', 'updated_at']

    def get_total_donations(self, obj):
        return obj.total_donations()

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ['id', 'project', 'donor_name', 'amount', 'created_at']