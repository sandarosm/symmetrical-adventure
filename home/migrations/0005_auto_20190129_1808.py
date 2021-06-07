# Generated by Django 2.1.5 on 2019-01-29 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190127_0856'),
    ]

    operations = [
        migrations.CreateModel(
            name='noticeUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='file')),
                ('thumb', models.ImageField(blank=True, default='default.png', upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='newsupdate',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='file'),
        ),
    ]
