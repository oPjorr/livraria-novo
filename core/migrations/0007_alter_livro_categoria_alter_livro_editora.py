# Generated by Django 4.0.6 on 2022-07-12 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_livro_categoria_alter_livro_editora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='livros', to='core.categoria'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='editora',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='livros', to='core.editora'),
        ),
    ]