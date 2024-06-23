from django.db import models

# Create your models here.
class fotografia(models.Model):
    OPCOES_CATGORIA = [
        ("NEBULOSA","Nebulosa"),
        ("ESTRELA","Estrela"),
        ("GALÁXIA","Galáxia"),
        ("PLANETA","Planeta")
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100,choices=OPCOES_CATGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return f" Fotografia [nome={self.nome}]"


