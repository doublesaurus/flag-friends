from django.core.management.base import BaseCommand
from main.models import Country
import requests
import logging

logger = logging.getLogger(__name__)

REST_COUNTRIES_API = "https://restcountries.com/v3.1"

# python manage.py seed --mode=clear

"""Clear data and do not create any objects in the database"""

MODE_CLEAR = 'clear'

class Command(BaseCommand):
    help = "Fetch country data to seed the database"

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def delete_countries():
    """Deletes all the country data"""
    logger.info("Delete Country records")

    Country.objects.all().delete()


def seed_countries():
    """Fetches country data and parses it out to seed the database"""
    logger.info("Fetching country data")

    response = requests.get(f"{REST_COUNTRIES_API}/all")

    print(response.json())

    country = Country(
        name="United States",
        symbol="USA"
    )

   #country.save()
   #logger.info("{} country created.".format(country))

def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear
    :return:
    """

    delete_countries()

    if mode == MODE_CLEAR:
        return

    seed_countries()