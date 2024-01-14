# WatchMe - Online Movie Rental
![Logo](https://i.imgur.com/KejfKMV.png)

## Description
WatchMe is an application developed using the Python language and the Django framework. It is used to operate an online movie rental service. It offers easy management of movies, users and administrators. It displays notifications of all activities and allows you to rent movies for a period of 7 days.

## Features:
- **Create/Read/Update/Delete:**
  - Movie
  - Author
  - User
  - AdminUser
- **User Actions:**
  - Register
  - Login
  - Logout
- **Movie Actions:**
  - Search for a movie
  - Rent Movie (default for 7 days)
  - View Rented Movies
  - View movie details
- **Other:**
  - Alerts after all operations (add, edit, delete, search, login, logout, rent, end of rent, etc.)
  - "Coins" as currency


##Data Model Diagram
![Database diagram](screenshots/database_diagram.svg)

## Endpoints
| Action             | Endpoint               | Auth          |
|--------------------|------------------------|---------------|
| Home Page          | `/store/`              | **Everyone**  |
| Search Movie       | `/store/movie/search`  | **Everyone**  |
| Registration       | `/store/register`      | **Everyone**  |
| Login              | `/store/login`         | **Everyone**  |
| Movie Details      | `/store/movie/details` | **Everyone**  |
| Logout             | `/store/logout`        | **Logged in** |
| User Details       | `/store/user/details`  | **Logged in** |
| Rented Movies      | `/store/user/rented`   | **Logged in** |
| Add Coins          | `/store/user/addcoins` | **Logged in** |
| Rent Movie         | `/store/movie/rent?id` | **Logged in** |
| Add Movie          | `/store/movie/add`     | **Superuser** |
| Movie Edit List    | `/store/movie/list`    | **Superuser** |
| Edit Movie Details | `/store/movie/edit?id` | **Superuser** |
| Delete Movie       | `/store/movie/delete`  | **Superuser** |
| Django Admin Panel | `/admin`               | **Superuser** |

##Screenshots

###Home Page
![HomePage](screenshots/HomePage.png)

###Search Movie Results List Page
![SearchResultPage](screenshots/SearchResultPage.png)

<!--###Register Form Page
![RegisterPage](screenshots/RegisterPage.png)-->

###User Exist Alert on Register Page
![UserExistAction](screenshots/UserExistAction.png)

###Login Form Page and Bad Credentials Alert
![BadLoginAction](screenshots/BadLoginAction.png)

###Movie Details Page
![DetailsPage](screenshots/DetailsPage.png)

###Edit User Details Form Page and Edit Alert
![ChangedUserDetails](screenshots/ChangedUserDetails.png)

###Rented Movies List Page
![RentedMoviePage](screenshots/RentedMoviePage.png)

###Add Coins Form Page
![AddCoins](screenshots/AddCoins.png)

###Rented Movie Success Alert on Movie Details Page
![RentMovieAction](screenshots/RentMovieAction.png)

###Add Movie Form Page and Added Movie Success Alert
![AddedMovieAction](screenshots/AddedMovieAction.png)

###Movies Edit or Delete List Page and Edited Success Alert
![EditedMovieAction](screenshots/EditedMovieAction.png)

###Edit Movie Form Page
![EditMoviePage](screenshots/EditMoviePage.png)

###User Actions Panel
![UserExistAction](screenshots/UserPanel.png)

###Admin Actions Panel
![adminPanel](screenshots/AdminPanel.png)

###Lost Access To Watch Movie Alert on Home Page
![LostAccessToMovie](screenshots/LostAccessToMovie.png)

###Unauthorized Alert on Home Page
![Unauthorized](screenshots/Unauthorized.png)

###Admin Django Panel
![adminDjangoPanel](screenshots/adminDjango.png)

##Tech Stack
[![My Skills](https://skillicons.dev/icons?i=python,django,bootstrap,sqlite,html&theme=light)](https://skillicons.dev)

## Author
- [@Oskar Wal](https://github.com/OskarWal)
