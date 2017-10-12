# -*- coding: utf-8 -*-
# Generated by Django 1.11.5.dev20170816164241 on 2017-09-25 07:43
from __future__ import unicode_literals

from django.db import migrations


def migrate_acl(apps, schema_editor):
    Project = apps.get_model('trans', 'Project')

    ACCESS_PRIVATE = 100
    Project.objects.filter(
        enable_acl=True
    ).update(
        access_control=ACCESS_PRIVATE
    )


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0097_project_access_control'),
    ]

    operations = [
        migrations.RunPython(migrate_acl),
    ]