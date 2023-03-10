# Generated by Django 4.1.4 on 2022-12-26 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('nom', models.CharField(blank=True, max_length=200, null=True)),
                ('prenom', models.CharField(blank=True, max_length=200, null=True)),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('wilaya', models.CharField(choices=[('Bejaia', 'Bejaia')], max_length=100)),
                ('dairas', models.CharField(choices=[('Bejaia', 'Bejaia'), ('Chemini', 'Chemini')], max_length=100)),
                ('communes', models.CharField(choices=[('Bejaia', 'Bejaia'), ('Oued_ghir', 'Oued_ghir'), ('Chimini', 'Chimini'), ('Tibane', 'Tibane'), ('Souk_oufella', 'Souk_oufella'), ('Akfadou', 'Akfadou')], max_length=100)),
                ('adresse', models.CharField(max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Annonces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie', models.CharField(choices=[('primaire', 'primaire'), ('collége', 'collége'), ('lycée', 'lycée')], max_length=200)),
                ('theme', models.CharField(max_length=200)),
                ('modalite', models.CharField(choices=[('offline', 'offline'), ('online', 'online')], max_length=200)),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('tarif', models.IntegerField(default=0)),
                ('date_publication', models.DateTimeField(auto_now_add=True)),
                ('wilaya', models.CharField(choices=[('Bejaia', 'Bejaia')], max_length=100)),
                ('dairas', models.CharField(choices=[('Bejaia', 'Bejaia'), ('Chemini', 'Chemini')], max_length=100)),
                ('communes', models.CharField(choices=[('Bejaia', 'Bejaia'), ('Oued_ghir', 'Oued_ghir'), ('Chimini', 'Chimini'), ('Tibane', 'Tibane'), ('Souk_oufella', 'Souk_oufella'), ('Akfadou', 'Akfadou')], max_length=100)),
                ('adresse', models.CharField(max_length=200)),
                ('Annonceur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Annonce.profiles')),
            ],
        ),
    ]
