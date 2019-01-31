from datetime import timedelta

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils import timezone
from registration.models import RegistrationProfile


class Command(BaseCommand):
    help = 'Delete expired user registrations from the database'

    def handle(self,  *args,  **options):
        for profile in RegistrationProfile.objects.exclude(activated=True)\
                      .filter(user__date_joined__lt=timezone.now() - timedelta(days=settings.ACCOUNT_ACTIVATION_DAYS))\
                      .filter(user__is_active=False):
            if not profile.user.profile.submission_set.exists():
                profile.user.delete()
                profile.delete()
