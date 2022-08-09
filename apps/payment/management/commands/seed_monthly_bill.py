import random

from course.models import Course
from django.core.management.base import BaseCommand
from django_seed import Seed




class Command(BaseCommand):
    help = 'This command creates monthly bills'

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many monthly bills do you want to create?")

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        seeder.add_entity(Course, number,
                          {
                              'price': random.randint(0, 5000000),
                              'fixed_percentage': random.randint(10, 100),
                              'salary': random.randint(1200000, 30000000),
                          })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} monthly bills created!"))

