# Generated by Django 4.0.3 on 2022-07-14 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_alter_contact_us_is_read_by_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='uploaded_files')),
            ],
        ),
    ]
