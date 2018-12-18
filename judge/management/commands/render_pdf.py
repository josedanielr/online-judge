import os
import shutil
import sys

from django.conf import settings
from django.core.management.base import BaseCommand
from django.template.loader import get_template
from django.utils import translation

from judge.models import Problem, ProblemTranslation
from judge.pdf_problems import DefaultPdfMaker, PhantomJSPdfMaker, SlimerJSPdfMaker


class Command(BaseCommand):
    help = 'renders a PDF file of a problem'

    def add_arguments(self, parser):
        parser.add_argument('code', help='code of problem to render')
        parser.add_argument('directory', nargs='?', help='directory to store temporaries')
        parser.add_argument('-l', '--language', default=settings.LANGUAGE_CODE,
                            help='language to render PDF in')
        parser.add_argument('-p', '--phantomjs', action='store_const', const=PhantomJSPdfMaker,
                            default=DefaultPdfMaker, dest='engine')
        parser.add_argument('-s', '--slimerjs', action='store_const', const=SlimerJSPdfMaker, dest='engine')

    def handle(self, *args, **options):
        try:
            problem = Problem.objects.get(code=options['code'])
        except Problem.DoesNotExist:
            print 'Bad problem code'
            return

        try:
            trans = problem.translations.get(language=options['language'])
        except ProblemTranslation.DoesNotExist:
            trans = None

        directory = options['directory']
        with options['engine'](directory, clean_up=directory is None) as maker, \
                translation.override(options['language']):
            maker.html = get_template('problem/raw.html').render({
                'problem': problem,
                'problem_name': problem.name if trans is None else trans.name,
                'description': problem.description if trans is None else trans.description,
                'url': '',
                'math_engine': maker.math_engine,
            }).replace('"//', '"https://').replace("'//", "'https://")

            # replace also local relative urls in html
            base_url = "http://" + settings.ALLOWED_HOSTS[0] + "/"
            maker.html = maker.html.replace('"/', '"' + base_url).replace("'/", "'" +  base_url)

            for file in ('style.css', 'pygment-github.css', 'mathjax_config.js'):
                maker.load(file, os.path.join(settings.DMOJ_RESOURCES, file))
            maker.make(debug=True)
            if not maker.success:
                print>>sys.stderr, maker.log
            elif directory is None:
                shutil.move(maker.pdffile, problem.code + '.pdf')
