import datetime
from datetime import date

import django.contrib.auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.
from django.utils import timezone

from store.forms import RegisterForm, LoginForm, MovieForm, AddCoinsForm, EditMovieForm, EditUserForm
from store.models import UserProfile, Movie, MovieRented


def register(request):
    check_deadline(request)
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd.get('login')
            password = cd.get('password')
            email = cd.get('email')
            name = cd.get('name')
            surname = cd.get('surname')
            birthdate = cd.get('birthdate')
            user, created = User.objects.get_or_create(username=username)
            if(created):
                user.email = email
                user.first_name = name
                user.last_name = surname
                user.set_password(password)
                profile = UserProfile.objects.get(user=user)
                profile.birth_date = birthdate
                profile.save(update_fields=["birth_date"])
                user.save()
                messages.success(request, 'Konto zostało utworzone. Możesz się zalogować')
            else:
                messages.warning(request, 'Uzytkownik istnieje w bazie danych')

    if not request.user.is_authenticated:
        form = RegisterForm()
        return render(request, 'registerPage.html', {'form':form})
    else:
        return redirect('/store')

def login(request):
    check_deadline(request)
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd.get('login')
            password = cd.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                django.contrib.auth.login(request, user)
            else:
                messages.warning(request, 'Niepoprawny login lub haslo')

    if request.user.is_authenticated:
        return redirect('/store')
    else:
        form = LoginForm()
        return render(request, 'loginPage.html', {'form':form})

def home(request):
    check_deadline(request)
    data = Movie.objects.all().order_by('-pk')
    return render(request, 'homePage.html',{'data':data})

def addMovie(request):
    check_deadline(request)
    if request.user.is_superuser:
        if request.method == 'POST':
            form = MovieForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                title = cd.get('title')
                price = cd.get('price')
                category = cd.get('category')
                soundtrack = cd.get('soundtrack')
                language = cd.get('language')
                description = cd.get('description')
                subtitles = cd.get('subtitles')
                subtitles_language = cd.get('subtitles_language')
                picture_url = cd.get('picture_url')
                if(subtitles):
                    new_movie = Movie(title=title,price=price,category=category,soundtrack=soundtrack,
                                  language=language,description=description,subtitles=True,subtitles_language=subtitles_language,picture_url=picture_url )
                else:
                    new_movie = Movie(title=title, price=price, category=category, soundtrack=soundtrack,
                                      language=language, description=description, subtitles=False, picture_url=picture_url)
                new_movie.save()

                messages.success(request, 'Dodano film')
                return redirect('/store/movie/add')
            else:
                messages.error(request, 'Błąd dodania')
        else:
            form = MovieForm()
            return render(request, "addMovie.html", {'form': form})
    else:
        messages.warning(request, 'Brak uprawnień')
        return redirect('/store')


def movieDetails(request):
    check_deadline(request)
    id = request.GET["id"]
    movie = Movie.objects.get(id=id)
    is_rented = False
    if request.user.is_authenticated:
        user = request.user
        movies = MovieRented.objects.filter(movie=movie, user=user)
        if(movies.count() > 0):
            is_rented = True

    return render(request, "movieDetails.html",{'movie': movie, 'rented' : is_rented})

def logout(request):
    check_deadline(request)
    django.contrib.auth.logout(request)
    return redirect("/store")

def userDetails(request):
    check_deadline(request)
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        profile = UserProfile.objects.get(user=user)
        if request.method == "POST":
            form = EditUserForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                email = cd.get('email')
                password = cd.get('password')
                name = cd.get('name')
                surname = cd.get('surname')
                birthdate = cd.get('birthdate')

                user.email = email
                user.first_name = name
                user.last_name = surname
                profile.birth_date = birthdate
                if password != "":
                    user.password = password
                user.save()
                profile.save()
                messages.success(request, "Zmieniono dane")
                return redirect("/store/user/details")
            else:
                messages.warning(request, "Błędne dane")
                return render(request, "userDetails2.html", {'form': form, 'user': user, 'profile': profile})
        else:
            form = EditUserForm()
            form.fields['email'].initial = user.email
            form.fields['name'].initial = user.first_name
            form.fields['surname'].initial = user.last_name
            form.fields['birthdate'].initial = profile.birth_date
            return render(request, "userDetails2.html", {'form' : form, 'user' : user, 'profile' : profile})
    else:
        messages.warning(request, "Zaloguj się")
        return redirect("/store")

def movieRented(request):
    check_deadline(request)
    if request.user.is_authenticated:
        data = MovieRented.objects.filter(user=request.user).order_by('-end_date')
        return render(request,"moviesRented.html",{'data' : data})
    else:
        messages.warning(request, "Zaloguj się")
        return redirect("/store")

def addCoins(request):
    check_deadline(request)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddCoinsForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                count = cd.get('count')
                if count > 0:
                    user = UserProfile.objects.get(user=request.user)
                    user.coins += count
                    user.save()
                    messages.success(request, "Doładowano " + str(count) + " monet")
                    return redirect("/store")
                else:
                    messages.warning(request, "Niepoprawna liczba")
                    return redirect("/store")
        else:
            form = AddCoinsForm()
            return render(request, 'addCoins.html', {'form': form})
    else:
        messages.warning(request, "Zaloguj się")
        return redirect("/store")

def rentMovie(request):
    check_deadline(request)
    if request.user.is_authenticated:
        id = request.GET["id"]
        movie = Movie.objects.get(id=id)
        user = request.user
        profile = UserProfile.objects.get(user=user)
        if profile.coins >= movie.price:
            movie_rent, created = MovieRented.objects.get_or_create(movie=movie, user=user)
            if created:
                old_coins = profile.coins
                profile.coins = old_coins - movie.price
                profile.save()
                movie_rent.save()
                messages.success(request,"Wypożyczono film")
                return redirect("/store/movie/details?id=" + id)
            else:
                messages.success(request,"Posiadasz już ten film")
                return redirect("/store/movie/details?id=" + id)
        else:
            messages.success(request, "Niewystrczająca ilość monet")
            return redirect("/store/movie/details?id=" + id)
    else:
        messages.warning(request,"Zaloguj się")
        return redirect("/store")

def editList(request):
    check_deadline(request)
    if request.user.is_superuser:
        data = Movie.objects.all().order_by('-pk')
        return render(request, 'editList.html', {'data': data})
    else:
        messages.warning(request, "Brak dostępu")
        return redirect("/store")

def editMovie(request):
    check_deadline(request)
    if request.user.is_superuser:
        if request.method == 'POST':
            form = EditMovieForm(request.POST)
            if form.is_valid():
                id = request.GET["id"]

                cd = form.cleaned_data
                title = cd.get('title')
                price = cd.get('price')
                category = cd.get('category')
                soundtrack = cd.get('soundtrack')
                language = cd.get('language')
                description = cd.get('description')
                subtitles = cd.get('subtitles')
                subtitles_language = cd.get('subtitles_language')
                picture_url = cd.get('picture_url')

                movie = Movie.objects.get(id=id)
                movie.title = title
                movie.price = price
                movie.category = category
                movie.soundtrack = soundtrack
                movie.language = language
                movie.description = description
                movie.subtitles = subtitles
                movie.subtitles_language = subtitles_language
                movie.picture_url = picture_url
                movie.save()
                messages.success(request, 'Dokonano edycji')
                return redirect('/store/movie/list')
            else:
                messages.error(request, 'Błąd dodania')
        else:
            id = request.GET["id"]
            movie = Movie.objects.get(id=id)
            form = EditMovieForm()

            form.fields['title'].initial = movie.title
            form.fields['price'].initial = movie.price
            form.fields['category'].initial = movie.category
            form.fields['soundtrack'].initial = movie.soundtrack
            form.fields['language'].initial = movie.language
            form.fields['description'].initial = movie.description
            form.fields['subtitles'].initial = movie.subtitles
            form.fields['subtitles_language'].initial = movie.subtitles_language
            form.fields['picture_url'].initial = movie.picture_url

            return render(request, "editMovie.html", {'form': form})
    else:
        messages.warning(request, 'Brak uprawnień')
        return redirect('/store')

def deleteMovie(request):
    check_deadline(request)
    if request.user.is_superuser:
        id = request.GET["id"]
        movie = Movie.objects.get(id=id)
        movie.delete()
        messages.success(request, 'Usunięto film')
        return redirect('/store/movie/list')
    else:
        messages.warning(request, 'Brak uprawnień')
        return redirect('/store')


def searchMovie(request):
    check_deadline(request)
    if request.method == "POST":
        searchfor = request.POST['searchfor']

        lookups = Q(title__icontains=searchfor) | Q(language__icontains=searchfor) | Q(soundtrack__icontains=searchfor) | Q(category__icontains=searchfor)

        data = Movie.objects.filter(lookups).order_by('-pk')
        messages.success(request, "Wyniki wyszukiwania dla: " + searchfor)
        return render(request, 'homePage.html', {'data': data})
    else:
        return redirect("/store")

def check_deadline(request):
    if request.user.is_authenticated:
        movie_rented = MovieRented.objects.filter(user=request.user)
        for movie in movie_rented:
            if movie.end_date < timezone.now():
                messages.warning(request,"Utraciłeś dostęp do filmu: " + movie.movie.title + "  (Powód: koniec okresu wypożyczenia)")
                movie.delete()