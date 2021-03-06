# Generated by Django 2.2 on 2019-05-01 14:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.PositiveIntegerField(db_index=True, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('e_mail', models.EmailField(max_length=254)),
                ('contnet', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('page_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='pages.Page')),
                ('profile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='profiles.Profile')),
            ],
            options={
                'db_table': 'pl_comments',
            },
        ),
    ]
