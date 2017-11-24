from django.core.management.base import BaseCommand, CommandError
from news.models import News
from news.models import Membres
import csv

class Command(BaseCommand):

    def handle(self, *args, **options):
        n = 0
        with open('membres_org.csv') as csvfile:
            members_reader = csv.reader(csvfile, delimiter=',')
            for row in members_reader:

                mb, created = Membres.objects.get_or_create(
                    nummer= int(row[0]),
                    mandantnummer = int(row[1]),
                    anrede = row[2],
                    titel = row[3],
                    vorname = row[4],
                    nachname = row[5],
                    firma = row[6],
                    zusatz = row[7],
                    postfach = row[8],
                    strasse = row[9],
                    plz = int(row[10]),
                    ort = row[11],
                    kanton = row[12],
                    land = row[13],
                    austrittsgrund = row[14],
                    email = row[15],
                    geschaeft_phone = row[16],
                    mobile_phone = row[17],
                    schulhaus = row[18],
                    fachverband = row[19]
                )
                if created:
                    n += 1
                else:
                    print("not created")
        self.stdout.write(self.style.SUCCESS('%s members loaded.' % n))







