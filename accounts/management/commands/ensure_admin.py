import os

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create or update the production admin account from environment variables."

    def handle(self, *args, **options):
        username = os.environ.get("ADMIN_USERNAME", "").strip()
        password = os.environ.get("ADMIN_PASSWORD", "")
        email = os.environ.get("ADMIN_EMAIL", "").strip()

        if not username or not password:
            self.stdout.write(
                self.style.WARNING(
                    "ADMIN_USERNAME/ADMIN_PASSWORD not set; skipping admin bootstrap."
                )
            )
            return

        user, created = User.objects.get_or_create(
            username=username,
            defaults={"email": email},
        )

        if email and user.email != email:
            user.email = email

        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()

        profile = user.profile
        if profile.role != "admin":
            profile.role = "admin"
            profile.save(update_fields=["role"])

        status = "created" if created else "updated"
        self.stdout.write(
            self.style.SUCCESS(f"Production admin '{username}' {status} successfully.")
        )
