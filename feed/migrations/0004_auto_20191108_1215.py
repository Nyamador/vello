# Generated by Django 2.2.6 on 2019-11-08 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_auto_20191107_1319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reaction',
            old_name='verb',
            new_name='kind',
        ),
    ]
