import os
import zipfile

from django.core.management.base import BaseCommand
from django.db.models import F

from judge.models import ContestSubmission


class Command(BaseCommand):
    help = "exports all finally accepted contest's submissions"
    PROJ_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))

    def add_arguments(self, parser):
        parser.add_argument('code', help='contest code')
        parser.add_argument('-a','--all', action='store_true', help='output all submissions')

    def handle(self, *args, **options):
        contest_code = options['code']

        cont_sub = ContestSubmission.objects.filter(participation__contest__key=contest_code, participation__virtual=0)
        cont_sub = cont_sub \
            .annotate(user=F('submission__user__user__username'), cod_problem=F('submission__problem__code'),
                      sub_id=F('submission__id'), source=F('submission__source'), ext=F('submission__language__key')) \
            .values('user', 'cod_problem', 'points', 'sub_id', 'source', 'ext') \
            .order_by('-points')

        self.create_zip(contest_code + '_' + ('all' if options['all'] else 'ok'))
        
        if options['all']:
            for t in cont_sub:
                self.write_to_zip(t['user'], t['cod_problem'], t['sub_id'], t['source'], t['ext'])
        else:
            user_points = []
            prob_id = {}
            prob_count = 0

            for t in cont_sub:
                if t['cod_problem'] not in prob_id:
                    user_points.append({})
                    prob_id[t['cod_problem']] = prob_count
                    prob_count += 1
                    
                act_id = prob_id[t['cod_problem']]

                if t['user'] not in user_points[act_id]:
                    user_points[act_id][t['user']] = t['points']

                if t['points'] == user_points[act_id][t['user']]:
                    self.write_to_zip(t['user'], t['cod_problem'], t['sub_id'], t['source'], t['ext'])

        self.close_zip()

    def write_to_zip(self, user, problem, sub_id, src, lang):
        #print('user: %s, problem %s, submission %d.%s, src size %d' % (user, problem, sub_id, lang, len(src)))

        path = [user, problem, str(sub_id) + '.' + lang]
        self._zip.writestr('/' + '/'.join(path), src.encode('utf-8').strip())

    def create_zip(self, name):
        self._zip = zipfile.ZipFile("%s.zip" % name, "w", zipfile.ZIP_DEFLATED)

    def close_zip(self):
        self._zip.close()
