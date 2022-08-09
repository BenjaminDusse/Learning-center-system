import random
from django.core.management.base import BaseCommand, CommandError
from django_seed import Seed
from center.models import Center
from course.models import Course


class Command(BaseCommand):
    help = 'This command creates courses'

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",  default=2, type=int, help="How many courses do you want to create?")

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_centers = Center.objects.all()
        seeder.add_entity(Course, number,
                          {
                              'center': lambda x: random.choice(all_centers),
                              "name": lambda x: seeder.faker.name(),
                              'price': lambda x: random.randint(300000, 1000000),
                          })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} courses created!"))
