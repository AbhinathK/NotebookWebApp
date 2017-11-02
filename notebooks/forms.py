from .models import Note
from django import forms

class NoteSearchForm(forms.Form):
    search_title =  forms.CharField(
                    required = False,
                    label='Search title',
                    widget=forms.TextInput(attrs={'placeholder': 'Search'})
                  )

    search_author =  forms.CharField(
                    required = False,
                    label='Search author',
                    widget=forms.TextInput(attrs={'placeholder': 'Search'})
                  )

    search_description =  forms.CharField(
                    required = False,
                    label='Search description',
                    widget=forms.TextInput(attrs={'placeholder': 'Search'})
                  )
