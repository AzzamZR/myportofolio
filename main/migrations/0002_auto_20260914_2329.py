from django.db import migrations
from django.core.management import call_command

def load_initial_data(apps, schema_editor):
    call_command('loaddata', 'experiences.json')

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_initial_data),
    ]