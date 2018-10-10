from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Cadastro(models.Model):
    sex = (
        ('0', 'Masculino'),
        ('1', 'Feminino'),
    )
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nome = models.TextField(max_length=20)
    telefone = models.TextField(max_length=20)
    idade= models.TextField(max_length=20)
    email = models.EmailField()
    rg = models.TextField(max_length=20)
    sexo = models.CharField(max_length=1, choices=sex)
    created_date = models.DateField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nome
