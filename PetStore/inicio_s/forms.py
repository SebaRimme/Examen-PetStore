from django.forms import (
    Form,
    CharField,
    PasswordInput,
    EmailField,
    EmailInput,
    CheckboxInput,
    BooleanField,
    TextInput
)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroUsuario(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['password1'].widget.attrs = { 'class':'form-control' }
        self.fields['password2'].widget.attrs = { 'class':'form-control' }

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'email'
        ]
        widgets = {
            'username': TextInput(
                attrs = {
                    'class':'form-control'
                }
            ),
            'first_name': TextInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'last_name': TextInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'email': EmailInput(
                attrs = {
                    'class':'form-control'
                }
            )
        }

class FormularioSesion(Form):
    
    nombre_usuario = CharField(
        required = True,
        label = 'Ingrese su nombre',
        widget = TextInput(
            attrs = {
                'class':'form-control',
                'placeholder':'Nombre123'
            }
        )
    )

    contrasenia_usuario = CharField(
        required = True,
        min_length = 6,
        max_length = 12,
        label = 'Ingrese su contraseña',
        widget = PasswordInput(
            attrs = {
                'class':'form-control',
                'placeholder':'Contraseña'
            }
        )
    )
    
    recuerdame = BooleanField(
        required = False,
        label = 'Recordarme',
        widget = CheckboxInput(
        )
    )