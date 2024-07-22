import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

#install django-extensions and run the following command to run the script
#the script will load the data from meow.csv to the database
# python3 manage.py runscript cats_load

from cats.models import Cat, Breed

def run():
    fhand = open('cats/meow.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Cat.objects.all().delete()
    Breed.objects.all().delete()

    # Name,Breed,Weight
    # Abby,Sphinx,6.4
    # Annie,Burmese,7.6
    # Ash,Manx,7.8
    # Athena,Manx,8.9
    # Baby,Tabby,6.9

    for row in reader:
        print(row)

        b, created = Breed.objects.get_or_create(name=row[1])

        c = Cat(nickname=row[0], breed=b, weight=row[2])
        c.save()
