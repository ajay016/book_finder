from django import forms
from .models import *

class AddBookForm(forms.ModelForm):
    authors = forms.CharField(max_length=255, required=False)
    genres = forms.CharField(max_length=255, required=False)

    class Meta:
        model = Book
        fields = '__all__'

    # def save(self, commit=True):
    #     book = super().save(commit=False) # get the instance
    #     if commit:
    #         book.save()# normally save the book
    #     authors = self.cleaned_data.get('authors') # get the authors (ids also valid)
    #     if authors:
    #         book.author_set.set(authors) # set the authors to the book
    #     return book


class AddAuthorForm(forms.ModelForm):
    
    class Meta:
        model = Author
        fields = '__all__'
        

