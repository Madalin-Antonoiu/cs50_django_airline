## Create project
1. django-admin startproject cs50_django_airline
2. cd cs50_django_airline

## Add an app
3. py manage.py startapp flights
4. settings.py > Add to INSTALLED_APPS += flights
5. urls.py > Add flights to path
```py
 from django.contrib import admin
 from django.urls import path, include #+

urlpatterns = [
    path('admin/', admin.site.urls),
    path('flights/', include("flights.urls")), #+
]

```
6. flights/ add urls.py > 
```py
    from django.urls import path
    from . import views

    app_name = "flights"
    urlpatterns = [
    # Models.py first
    ]

```
## Add a model
7. flights/models.py
```py
from django.db import models

# Create your db models here.
class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()

    # This is to return formated string when querying db
    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}, duration {self.duration} min"
```
8. py manage.py makemigrations && py manage.py migrate  
    Inspecting db.sqlite3 we find these:
    [Vezi screenshot](https://prnt.sc/umujid)
9. To edit flights, py manage.py shell
```py
    >>> from flights.models import Flight   
    >>> f= Flight(origin="New York", destination="London", duration=415)
    >>> f.save()
    # To see that flight:
    >>> Flight.objects.all()

    # To delete
    >>> f.delete()
```

FULL DOCUMENTATION: https://cs50.harvard.edu/web/2020/notes/4/

Annoying pylint-django errors?   

`
pip install pylint-django   


Press ctr+sft+P to open the the Command Palette. Now in command palette type Preferences: Configure Language Specific Settings. Now select Python. Add a coma and paste this:
```py
"python.linting.pylintArgs": [
        "--load-plugins=pylint_django",
        "--errors-only"
    ]
```


Hope this will help!
`