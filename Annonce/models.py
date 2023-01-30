from django.forms import ModelForm
from django.db import models
import uuid
from django.contrib.auth.models import User



class Profiles(models.Model): 
    wilaya = (
        ('Bejaia', 'Bejaia'),
    )
    dairas = (
        ('Bejaia', 'Bejaia'),
        ('Chemini', 'Chemini'),
        
    )
    communes = (
        ('Bejaia', 'Bejaia'),
        ('Oued_ghir', 'Oued_ghir'),
        ('Chimini', 'Chimini'),
        ('Tibane', 'Tibane'),
        ('Souk_oufella', 'Souk_oufella'),
        ('Akfadou', 'Akfadou')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    nom = models.CharField(max_length=200, null = True, blank=True)
    prenom = models.CharField(max_length=200, null = True, blank=True)
    username = models.CharField(max_length=200, null = True, blank=True)
    profile_image = models.ImageField(null=True, blank=True)
    wilaya = models.CharField(choices=wilaya, max_length=100)
    dairas = models.CharField(choices=dairas, max_length=100)
    communes = models.CharField(choices=communes, max_length=100)
    adresse = models.CharField(max_length=200, null=False, blank=False)

    id = models.UUIDField(default=uuid.uuid4, unique = True, primary_key=True, editable=False)

    def __str__(self):
        return self(self.user.username)

class adresseForm(ModelForm):
    class Meta:
        model = Profiles
        fields = ['wilaya', 'dairas', 'communes']
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['wilaya'].widget.attrs.update({'class': 'm-0'})

class Annonces(models.Model): #missed
    wilaya = (
        ('Bejaia', 'Bejaia'),
    )
    dairas = (
        ('Bejaia', 'Bejaia'),
        ('Chemini', 'Chemini'),
        
    )
    communes = (
        ('Bejaia', 'Bejaia'),
        ('Oued_ghir', 'Oued_ghir'),
        ('Chimini', 'Chimini'),
        ('Tibane', 'Tibane'),
        ('Souk_oufella', 'Souk_oufella'),
        ('Akfadou', 'Akfadou')
    )
    CAT_TYPE =(
        ('primaire', 'primaire'),
        ('collége', 'collége'),
        ('lycée', 'lycée')
    )
    MOD_TYPE =(
        ('offline', 'offline'),
        ('online', 'online')
    )
    Annonceur = models.ForeignKey(Profiles,null=True, blank=True, on_delete=models.SET_NULL)
    categorie = models.CharField(max_length=200, choices=CAT_TYPE)
    theme = models.CharField(max_length=200)
    modalite = models.CharField(max_length=200, choices=MOD_TYPE)
    description = models.TextField(max_length=2000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    tarif = models.IntegerField(default = 0)
    date_publication = models.DateTimeField(auto_now_add=True)
    wilaya = models.CharField(choices=wilaya, max_length=100)
    dairas = models.CharField(choices=dairas, max_length=100)
    communes = models.CharField(choices=communes, max_length=100)
    adresse = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.theme