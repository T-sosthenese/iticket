# Generated by Django 4.0.10 on 2024-01-08 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_alter_ticket_engineer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='contact_mode',
        ),
    ]
