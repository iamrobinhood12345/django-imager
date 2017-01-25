# django-imager

ImagerProfile

Intantiates a model instance connected to a User instance that allows for the user to add:  -Username -Camera -Photography Type -Employable? -Address -About Me -Website -Phone -Travel Radius 

Photo

Instantiates a model instance connected to a single ImagerProfile and possibly but not necessarily connected to an album or many albums.  -title -description -date_uploaded -date_modified -date_published -published 'Private' 'Shared' 'Public' -image to upload -albums 

Album

Instantiates a model instance connected to a single ImagerProfile and many pictures.  -title -description -date_uploaded -date_modified -date_published -published 'Private' 'Shared' 'Public' -cover -photos 

URLS

```
-"/admin" - Links to the admin login page
-"/" - links to the home page
-"/registration/" - a prefix to get to various registration pages listed below:
    -"/register" - links to registration page
    -"/activate/[ACTIVATION KEY]" - activates a profile with the key they are authorized to use
    -"/registration_complete" - shows a valid completed registration page
-"/login" - Links to the login page
-"/logout" - Logs the user out
```