from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Create an admin user'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='The username of the admin user')
        parser.add_argument('email', type=str, help='The email of the admin user')
        parser.add_argument('password', type=str, help='The password for the admin user')

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        email = kwargs['email']
        password = kwargs['password']

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f'User "{username}" already exists.'))
        else:
            User.objects.create_superuser(username=username, email=email, password=password,role='admin')
            self.stdout.write(self.style.SUCCESS(f'Admin user "{username}" created successfully.'))
