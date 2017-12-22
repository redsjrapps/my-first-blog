from django.db import models
from django.utils import timezone
# Create your models here.

     # Sempre comece um nome de classe com uma letra maiúscula.
class Post(models.Model):#define o nosso modelo, onde class define um objeto e Post é o nome do nosso modelo
    author = models.ForeignKey('auth.User')#este é um link para outro modelo
    title = models.CharField(max_length=200)#define um texto com um número limitado de caracteres.
    text = models.TextField()#este é para textos longos, sem um limite. Será ideal para um conteúdo de post de blog
    created_date = models.DateTimeField(
        default = timezone.now)#este é uma data e hora.
    published_date = models.DateTimeField(
        blank = True, null = True)
   
   # identados na class Post por pertencer a esta        
    def publish(self):#nosso método, cujo nome é publish
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):#nosso método que retorna um valor título
        return self.title
        
