from django import forms

from main_app.models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('email', 'name', 'heading', 'description')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form__input', 'type': "email", 'name': 'email', 'id': 'email',
                                             'placeholder': 'Введите ваш email'}),
            'name': forms.TextInput(attrs={'class': 'form__input', 'type': "text", 'name': 'username', 'id': 'username',
                                           'placeholder': 'Введите ваш имя'}),
            'heading': forms.TextInput(attrs={'class': 'form__input', 'type': "text", 'name': 'title', 'id': 'title',
                                              'placeholder': 'Заголовок сообщения'}),
            'description': forms.Textarea(attrs={'class': 'form__input', 'name': 'desc', 'id': 'desc',
                                              'placeholder': 'Описание', 'cols': '30', 'rows': '10'}),
        }


