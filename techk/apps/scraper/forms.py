from django import forms

class SearchForm(forms.Form):
    choices = (
        ('title','Title'),
        ('price','Price'),
        ('description','Description'),
        ('upc','UPC'),
    )
    Attribute = forms.ChoiceField(choices=choices)
    Search = forms.CharField()
