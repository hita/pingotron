from django.core.management.base import BaseCommand, CommandError
from pingService import transponder

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        self.stdout.write("Executing...")
        transponder.updateTargets()
        self.stdout.write("Done")
        
