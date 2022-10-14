from django import forms
from menu.models import Menu

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['date','breakfast','lunch','dinner']
        labels = {
            'date': '날짜',
            'breakfast':'아침',
            'lunch':'점심',
            'dinner':'저녁',
        }

# class DateForm(forms.Form):
#     class Meta:
#         model = Menu
#         fields = ['date_of_meal']
#         labels = {
#             'date_of_meal':'날짜',
#         }