import random
from django.core.management.base import BaseCommand, CommandError
from django_seed import Seed
from group.models import Group
from course.models import Course


class Command(BaseCommand):
    help = 'This command creates groups'

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",  default=2, type=int, help="How many groups do you want to create?")

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_courses = Course.objects.all()
        seeder.add_entity(Group, number, {
            "name" : seeder.faker.name(),
            'course' : lambda x: random.choice(all_courses)
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} groups created!"))
