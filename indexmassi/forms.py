from django import forms

class Forma(forms.Form):
    ves = forms.FloatField(initial="40", label="Вес в кг", widget=forms.NumberInput(attrs={"class": "myfield"}),
                             min_value=1, max_value=500)
    rost = forms.FloatField(initial=1, label="Рост в см", widget=forms.NumberInput(attrs={"class": "myfield"}),
                            min_value=50, max_value=300)