# Generated by Django 4.2 on 2024-12-09 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0005_alter_userprofile_email'),
        ('buildings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('user', models.ManyToManyField(to='authentication.userprofile')),
                ('zone', models.ManyToManyField(to='buildings.zone')),
            ],
        ),
    ]
