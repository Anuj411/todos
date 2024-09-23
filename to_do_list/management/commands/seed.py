from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    help = "Seed Migrations."

    def __init__(self):
        self.user_class = get_user_model()
        super().__init__()

    def handle(self, *args, **options):
        apps = settings.LOCAL_APPS
        for app in apps:
            call_command("makemigrations", app.split(".")[-1])
        call_command("migrate")
        self.create_super_user()

    def create_super_user(self):
        if self.user_class.objects.filter(email=settings.ADMIN_EMAIL).exists():
            self.stdout.write("Admin account already exist")
            return False

        super_user = self.user_class.objects.create_superuser(
            username=settings.ADMIN_USERNAME,
            password=settings.ADMIN_PASSWORD,
            email=settings.ADMIN_EMAIL,
            role=self.user_class.ADMIN
        )

        self.stdout.write("Created {} admin account.".format(settings.ADMIN_EMAIL))
