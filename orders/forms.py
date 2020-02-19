from django import forms

class AddItemToCart(forms.Form):
    quantity = forms.IntegerField(min_value=1)
    color = forms.CharField()