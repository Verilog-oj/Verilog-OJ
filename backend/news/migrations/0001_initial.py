# Generated by Django 3.1 on 2020-09-18 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(help_text='News ID', primary_key=True, serialize=False)),
                ('title', models.CharField(help_text='News title', max_length=40)),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='News creation time')),
                ('content', models.TextField(help_text='News content')),
                ('related_files', models.ManyToManyField(blank=True, help_text='File attached with the news', to='file.File')),
            ],
        ),
    ]
