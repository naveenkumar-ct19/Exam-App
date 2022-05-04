# Generated by Django 3.1 on 2020-08-18 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0005_auto_20200817_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('desc', models.TextField(verbose_name='Description')),
                ('tutor', models.IntegerField(verbose_name='Tutor ID')),
            ],
        ),
        migrations.CreateModel(
            name='Enrollments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentId', models.IntegerField(verbose_name='Student ID')),
                ('tutorId', models.IntegerField(verbose_name='Tutor ID')),
                ('courseId', models.IntegerField(verbose_name='Course ID')),
            ],
        ),
    ]
