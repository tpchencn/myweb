# Generated by Django 2.1.7 on 2019-03-25 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0005_examplemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=20)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('topic', models.ForeignKey(on_delete=True, to='learning_logs.Topic')),
            ],
            options={
                'verbose_name_plural': 'ReadNote',
            },
        ),
    ]
