from django . urls import path
from . import views
urlpatterns = [
    path ( '' , views.home , name = 'home') ,
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('movie/add', views.addMovie, name="addMovie"),
    path('movie/details', views.movieDetails, name ="movieDetails"),
    path('logout', views.logout, name ="logout"),
    path('user/details', views.userDetails, name="userDetails"),
    path('user/rented', views.movieRented, name="movieRented"),
    path('user/addcoins', views.addCoins, name="addCoins"),
    path('movie/rent', views.rentMovie, name="rentMovie"),
    path('movie/list', views.editList, name="editlist"),
    path('movie/edit', views.editMovie, name="editMovie"),
    path('movie/delete', views.deleteMovie, name="deleteMovie"),
    path('movie/search', views.searchMovie, name="searchMovie")

]
