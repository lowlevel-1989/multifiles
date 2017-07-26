from rest_framework import serializers
from .models import Ticket, File

class FileSerializer(serializers.ModelSerializer):

    file = serializers.SerializerMethodField('get_file_url')

    def get_file_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.file.url)

    class Meta:
        model = File
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):

    files = FileSerializer(many=True, read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'
