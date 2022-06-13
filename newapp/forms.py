from django import forms


class myTestForm(forms.Form):
    name = forms.CharField(
        help_text="Enter a date between now and 4 weeks (default 3).")
