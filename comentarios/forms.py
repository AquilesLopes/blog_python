from django.forms import ModelForm
from .models import Comentario

class FormComentario(ModelForm):

    def clean(self):
        data = self.cleaned_data
        nome = data.get('nome_comentario')
        comentario = data.get('comentario')

        if len(nome) < 5:
            self.add_error('nome_comentario', 'O nome deve ter pelo menos 5 caracteres')

        if len(comentario) < 10:
            self.add_error('comentario', 'O comentário deve ter pelo menos 10 caracteres')


    class Meta:
        model = Comentario
        fields = ('nome_comentario', 'email_comentario', 'comentario')