# Generated by Django 4.2 on 2023-04-16 21:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_alter_writemodel_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('edit_time', models.DateTimeField(auto_now=True)),
                ('writing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.writemodel')),
                ('yazan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
                'db_table': 'comment',
            },
        ),
    ]