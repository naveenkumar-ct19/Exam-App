# Generated by Django 3.1 on 2020-08-18 10:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0006_courses_enrollments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Tutor'),
        ),
    ]