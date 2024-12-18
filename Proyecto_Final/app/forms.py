from django import forms
 
class Autoformulario(forms.Form):
    marca = forms.CharField()
    interno = forms.IntegerField()
    