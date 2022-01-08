from django import forms
from django.forms import widgets


class BookForm(forms.Form):
    author = forms.CharField(max_length=100,
                             required=True,
                             label="Имя",
                             error_messages={"required": "Поле обязательно для заполнения",
                                             "max_length": "Максимальная длина поля 100"})
    email = forms.EmailField(required=True, label="Статус",
                             error_messages={"required": "Поле обязательно для заполнения",
                                             "max_length": "Максимальная длина поля 100"}
                             )
    text = forms.CharField(max_length=2000, required=True, label="Текст",
                           widget=widgets.Textarea(attrs={"rows": 5, "cols": 50}),
                           error_messages={"required": "Поле обязательно для заполнения",
                                           "max_length": "Максимальная длина поля 2000"})
