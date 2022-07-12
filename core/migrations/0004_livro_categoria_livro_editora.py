# Generated by Django 4.0.6 on 2022-07-12 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_livro_alter_autor_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='categoria',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='livros', to='core.categoria'),
        ),
        migrations.AddField(
            model_name='livro',
            name='editora',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='livros', to='core.editora'),
        ),
    ]
