import random
import string

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from judge.models import *


class Command(BaseCommand):
    help = 'creates a user'

    @staticmethod
    def random_word(length=10):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def add_arguments(self, parser):
        parser.add_argument('file', help='file with usernames (one per line)')
        parser.add_argument('organization', help='organization')
        parser.add_argument('out_file', help='output file for generated passwords')

    def handle(self, *args, **options):
        accounts = open(options['out_file'], "w")
        with open(options['file']) as file:
            for name in file:
                name = name.strip()
                usr = User(username=name, email=name + '@nomail.com', is_active=True)

                passw = Command.random_word()
                usr.set_password(passw)
                usr.is_superuser = False
                usr.is_staff = False
                usr.save()

                profile = Profile(user=usr)
                profile.language = Language.objects.get(key='CPP11')
                profile.save()

                profile.organizations.add(Organization.objects.get(short_name=options['organization']))

                accounts.write("User: {}\t Password: {}\n".format(name, passw))

        file.close()
        accounts.close()
