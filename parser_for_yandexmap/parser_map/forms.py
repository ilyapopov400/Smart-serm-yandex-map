from django import forms


class FormSearchQuery(forms.Form):
    find = forms.CharField(label="запрос", help_text="введите свой поисковый запрос")


class FormAnswer(forms.Form):
    address = forms.CharField(label="адрес")
    phone = forms.CharField(label="телефон")
