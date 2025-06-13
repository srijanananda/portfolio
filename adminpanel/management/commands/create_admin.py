from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Creates a default admin user'

    def handle(self, *args, **options):
        if not User.objects.filter(username="srija").exists():
            User.objects.create_superuser("srija", "srijan1ga21is164@gmail.com", "7795260651jas")
            self.stdout.write(self.style.SUCCESS('Admin user created.'))
        else:
            self.stdout.write(self.style.WARNING('Admin user already exists.'))
