from django import forms
from .models import Vehiculo


class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo

        fields = [
            "marca",
            "modelo",
            "anio",
            "placa",
            "color",
            "activo",
        ]

        widgets = {
            "marca": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ejemplo: Nissan",
                }
            ),
            "modelo": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ejemplo: Versa",
                }
            ),
            "anio": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ejemplo: 2024",
                }
            ),
            "placa": forms.TextInput(
                attrs={
                    "class": "form-control text-uppercase",
                    "placeholder": "Ejemplo: ABC-123-A",
                }
            ),
            "color": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ejemplo: Blanco",
                }
            ),
            "activo": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }

    def clean_placa(self):
        placa = self.cleaned_data["placa"]
        return placa.strip().upper()