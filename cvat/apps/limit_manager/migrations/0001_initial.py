# Generated by Django 3.2.16 on 2022-11-28 08:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("organizations", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Limitation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "memberships",
                    models.PositiveIntegerField(blank=True, default=2, null=True),
                ),
                (
                    "organizations",
                    models.PositiveIntegerField(blank=True, default=1, null=True),
                ),
                ("tasks", models.PositiveIntegerField(default=10, null=True)),
                ("projects", models.PositiveIntegerField(default=3, null=True)),
                ("cloud_storages", models.PositiveIntegerField(default=10, null=True)),
                (
                    "tasks_per_project",
                    models.PositiveIntegerField(default=5, null=True),
                ),
                (
                    "webhooks_per_project",
                    models.PositiveIntegerField(default=10, null=True),
                ),
                (
                    "webhooks_per_organization",
                    models.PositiveIntegerField(blank=True, default=10, null=True),
                ),
                ("view_analytics", models.BooleanField(default=False)),
                ("lambda_requests", models.BooleanField(default=False)),
                (
                    "org",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="organizations.organization",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]