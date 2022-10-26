from turtle import textinput
from django import forms  
class todoform(forms.Form):
    text= forms.CharField(max_length=40,
                          widget=forms.TextInput(attrs={'class':'form-control','placeholder':' e.g. delete junk file',
                                                        'aria-label':'todo','aria-describedby':'add-btn'}))