# django-imager
[![Build Status](https://travis-ci.org/Copenbacon/django-imager.svg?branch=models-2)](https://travis-ci.org/Copenbacon/django-imager)
[![Coverage Status](https://coveralls.io/repos/github/Copenbacon/django-imager/badge.svg?branch=models-2)](https://coveralls.io/github/Copenbacon/django-imager?branch=models-2)

##ImagerProfile
Intantiates a model instance connected to a User instance that allows for the user to add:
    ```
    -Username
    -Camera
    -Photography Type
    -Employable?
    -Address
    -About Me
    -Website
    -Phone
    -Travel Radius
    ```

##URLS
    ```
    -"/admin" - Links to the admin login page
    -"/" - links to the home page
    -"/registration/" - a prefix to get to various registration pages listed below:
        -"/register" - links to registration page
        -"/activate/[ACTIVATION KEY]" - activates a profile with the key they are authorized to use
        -"/registration_complete" - shows a valid completed registration page
    -"/login" - Links to the login page
    -"/logout" - Logs the user out