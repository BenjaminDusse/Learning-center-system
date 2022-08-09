from django.core.management.base import BaseCommand, CommandError
from django_seed import Seed
from branch.models import Branch


class Command(BaseCommand):
    help = 'This command creates branches'

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",  default=2, type=int, help="How many branches do you want to create?")

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        seeder.add_entity(Branch, number)
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} branches created!"))
