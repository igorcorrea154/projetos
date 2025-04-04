from django.core.management.base import BaseCommand
from graf_site.models import Token
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Remove tokens com mais de 12 horas de criação'

    def handle(self, *args, **kwargs):
        limite = timezone.now() - timedelta(hours=12)
        expirados = Token.objects.filter(created_at__lt=limite)
        total = expirados.count()
        expirados.delete()
        self.stdout.write(self.style.SUCCESS(f'{total} token(s) expirados removidos.'))
