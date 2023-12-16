
from django import forms
from django.db.models.functions import datetime

from store.models import Movie


class DateInput(forms.DateInput):
    input_type = 'date'


textInput = forms.TextInput(attrs={"class": "form-control text-center"})
passwordInput = forms.PasswordInput(attrs={"class": "form-control text-center"})
emailInput = forms.EmailInput(attrs={"class": "form-control text-center"})
dateInput = DateInput(attrs={"class": "form-control text-center"})
numberInput = forms.NumberInput(attrs={"class": "form-control text-center"})
checkInput = forms.CheckboxInput(attrs={"class": "form-check m-auto text-center", "type":"checkbox"})
textSelect = forms.Select(attrs={"class": "form-select text-center"})
textArea = forms.Textarea(attrs={"class": "form-control"})



class RegisterForm(forms.Form):
    email = forms.CharField(widget=emailInput, label="Email", max_length=50, required=True)
    login = forms.CharField(widget=textInput, label="Login", max_length=50, required=True)
    password = forms.CharField(widget=passwordInput, label="Haslo", max_length=50, required=True)
    name = forms.CharField(widget=textInput, label="Imie", max_length=100, required=True)
    surname = forms.CharField(widget=textInput, label="Nazwisko", max_length=100, required=True)
    birthdate = forms.DateField(widget=dateInput, label="Data Urodzenia", required=True)

class LoginForm(forms.Form):
    login = forms.CharField(widget=textInput, label="Login", max_length=50, required=True)
    password = forms.CharField(widget=passwordInput, label="Haslo", max_length=50, required=True)


class MovieForm(forms.Form):
    title = forms.CharField(widget=textInput, label="Tytuł", max_length=200, required=True)
    price = forms.CharField(widget=numberInput, label="Cena", required=True)
    category = forms.CharField(widget=textInput, label="Kategoria", required=True)
    minimum_age = forms.ChoiceField(widget=textSelect, label="Ograniczenia wiekowe",choices=Movie.age_choices, required=True)
    soundtrack = forms.ChoiceField(widget=textSelect, label="Ścieżka dźwiękowa",choices=Movie.choices, required=True)
    language = forms.CharField(widget=textInput, label="Język",max_length=100, required=True)
    description = forms.CharField(widget=textArea,label="Opis", max_length=10000, required=True)
    subtitles = forms.BooleanField(widget=checkInput, label="Napisy",required=False)
    subtitles_language = forms.CharField(widget=textInput, label="Język napisów", required=False)
    picture_url = forms.CharField(widget=textInput, label="URL obrazka",required=True)

class AddCoinsForm(forms.Form):
    count = forms.IntegerField(widget=numberInput, label="Monety", required=True)

class EditMovieForm(forms.Form):
    title = forms.CharField(widget=textInput, label="Tytuł", max_length=200, required=True)
    price = forms.CharField(widget=numberInput, label="Cena", required=True)
    category = forms.CharField(widget=textInput, label="Kategoria", required=True)
    minimum_age = forms.ChoiceField(widget=textSelect, label="Ograniczenia wiekowe",choices=Movie.age_choices, required=True)
    soundtrack = forms.ChoiceField(widget=textSelect, label="Ścieżka dźwiękowa",choices=Movie.choices, required=True)
    language = forms.CharField(widget=textInput, label="Język",max_length=100, required=True)
    description = forms.CharField(widget=textArea,label="Opis", max_length=10000, required=True)
    subtitles = forms.BooleanField(widget=checkInput, label="Napisy",required=False)
    subtitles_language = forms.CharField(widget=textInput, label="Język napisów", required=False)
    picture_url = forms.CharField(widget=textInput, label="URL obrazka",required=True)

class EditUserForm(forms.Form):
    email = forms.CharField(widget=emailInput, label="Email", max_length=50, required=True)
    password = forms.CharField(widget=passwordInput, label="Haslo", max_length=50, required=False)
    name = forms.CharField(widget=textInput, label="Imie", max_length=100, required=True)
    surname = forms.CharField(widget=textInput, label="Nazwisko", max_length=100, required=True)
    birthdate = forms.DateField(widget=dateInput, label="Data Urodzenia", required=True)



