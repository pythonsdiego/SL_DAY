from django.db import models

class Topico(models.Model):
    """Um tópico sobre o qual o usuário está trabalhando."""
    texto = models.CharField(max_length=200)
    criado_em = models.DateTimeField(auto_now_add=True)    
    
    def __str__(self):
        """Retorna uma representação de string do modelo."""
        return self.texto


class Entrada(models.Model):
    """Algo específico tratado sobre determinado tópico."""
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE)
    texto = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entradas'
        
    def __str__(self):
        return f"{self.texto[:50]}..."