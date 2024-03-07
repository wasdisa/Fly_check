
from django import forms
from .models import Ammo,Smodel,Brands


class UAVForm(forms.ModelForm):
    class Meta:
        model = UAV
        fields = ['serial', 'name', 'brand', 'model', 'ammo', 'weight']

    def __init__(self, *args, **kwargs):
        super(UAVForm, self).__init__(*args, **kwargs)
        self.fields['brand'].queryset = Brands.objects.all()
        self.fields['model'].queryset = Smodel.objects.all()
        self.fields['ammo'].queryset = Ammo.objects.all()

        # Set default options
        self.fields['brand'].initial = Brands.objects.first()
        self.fields['model'].initial = Smodel.objects.first()
        self.fields['ammo'].initial = Ammo.objects.first()