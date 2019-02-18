from django.core.management.base import BaseCommand
from django.db.models import F

from judge.models import ContestSubmission


class Command(BaseCommand):
    help = "exports all valid contest's submissions"

    def add_arguments(self, parser):
        parser.add_argument('code', help='contest code')

    def handle(self, *args, **options):
        contest_code = options['code']

        cont_sub = ContestSubmission.objects.filter(participation__contest__key=contest_code, points__gt=0,
                                                    participation__virtual=0)
        cont_sub = cont_sub.annotate(user=F('submission__user__user__username'),
                                     cod_problem=F('submission__problem__code'), source=F('submission__source')).values(
            'user', 'cod_problem', 'source', 'points').order_by('-points')

        unique = 0
        user_points = {}
        for t in cont_sub:
            if t['user'] not in user_points:
                user_points[t['user']] = t['points']

            if t['points'] == user_points[t['user']]:
                unique += 1

        print(unique)
