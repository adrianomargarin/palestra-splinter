# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.contrib.auth import get_user_model



class Migration(migrations.Migration):

    def create_superuser(apps, schema_editor):
        User = get_user_model()
        User.objects.create_superuser(username="adrianomargarin",
                                      email="teste@exemplo.com", password="123456")

    dependencies = [
    ]

    operations = [
        #migrations.RunPython(create_superuser),
    ]
