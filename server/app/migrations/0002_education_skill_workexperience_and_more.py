# Generated by Django 4.2.6 on 2023-10-29 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(max_length=255, verbose_name='Institution Name')),
                ('field_of_study', models.CharField(max_length=255, verbose_name='Field of Study')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-start_date'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-start_date'],
            },
        ),
        migrations.RemoveField(
            model_name='menteeprofile',
            name='mentee_specific_field',
        ),
        migrations.RemoveField(
            model_name='mentorprofile',
            name='mentor_specific_field',
        ),
        migrations.AddField(
            model_name='customuser',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Prefer not to say', 'Prefer not to say')], default='Prefer not to say', max_length=20),
        ),
        migrations.AddField(
            model_name='customuser',
            name='year_of_birth',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='menteeprofile',
            name='education',
            field=models.ManyToManyField(blank=True, related_name='mentee_education', to='app.education'),
        ),
        migrations.AddField(
            model_name='menteeprofile',
            name='skills',
            field=models.ManyToManyField(blank=True, related_name='mentee_profiles', to='app.skill'),
        ),
        migrations.AddField(
            model_name='mentorprofile',
            name='skills',
            field=models.ManyToManyField(blank=True, related_name='mentor_profiles', to='app.skill'),
        ),
        migrations.AddField(
            model_name='mentorprofile',
            name='work_experience',
            field=models.ManyToManyField(blank=True, related_name='mentor_work_experience', to='app.workexperience'),
        ),
    ]