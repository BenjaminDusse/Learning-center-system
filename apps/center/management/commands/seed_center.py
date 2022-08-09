from django.core.management.base import BaseCommand, CommandError
from django_seed import Seed
from center.models import Center


class Command(BaseCommand):
    help = 'This command creates centers'

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",  default=2, type=int, help="How many centers do you want to create?")

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        seeder.add_entity(Center, number, {
            "name": lambda x: seeder.faker.name(),
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} centers created!"))
