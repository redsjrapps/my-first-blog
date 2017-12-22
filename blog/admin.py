from django.contrib import admin
from .models import Post# importando/incluindo o modelo Post(localizado em blog/models.py)
# Register your models here.


admin.site.register(Post)# tornando o modelos visível na página de administração com o register
