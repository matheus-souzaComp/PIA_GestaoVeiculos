# Generated by Django 4.2.1 on 2023-11-03 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servico',
            old_name='servico',
            new_name='veiculo',
        ),
        migrations.AddField(
            model_name='servico',
            name='operacao',
            field=models.ManyToManyField(to='servicos.categoriamanutencao'),
        ),
    ]
