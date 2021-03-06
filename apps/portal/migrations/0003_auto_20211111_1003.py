# Generated by Django 3.2.9 on 2021-11-11 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_rename_descricao3_quemsomos_descricao'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipeMembro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('imagem', models.ImageField(upload_to='core/imagens', verbose_name='Primeira imagem')),
                ('descricao', models.CharField(max_length=255, verbose_name='Descrição')),
                ('cargo', models.CharField(max_length=255, verbose_name='Cargo')),
                ('experiencia', models.CharField(max_length=255, verbose_name='Experiência')),
                ('formacao', models.CharField(max_length=255, verbose_name='Formação')),
                ('data', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Equipe',
                'verbose_name_plural': 'Equipes',
            },
        ),
        migrations.CreateModel(
            name='SecaoEquipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField(max_length=255, verbose_name='Título')),
                ('subtitulo', models.TextField(max_length=255, verbose_name='Subtítulo')),
                ('data', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Seção Equipe',
                'verbose_name_plural': 'Seção Equipe',
            },
        ),
        migrations.DeleteModel(
            name='Equipe',
        ),
        migrations.AddField(
            model_name='contatos',
            name='mapa',
            field=models.CharField(default=' ', max_length=500, verbose_name='Google Maps'),
            preserve_default=False,
        ),
    ]
