from tabnanny import verbose
from django.db import models


class Categoria(models.Model):
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao


class Editora(models.Model):
    nome = models.CharField(max_length=200)
    site = models.URLField()

    def __str__(self):
        return self.nome


class Autor(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Autores"

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=32)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="livros",
    )
    editora = models.ForeignKey(
        Editora, on_delete=models.PROTECT, related_name="livros",
    )
 
    def __str__(self):
        return f'{self.titulo} ({self.quantidade})'