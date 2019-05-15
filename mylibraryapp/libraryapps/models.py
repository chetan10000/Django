from django.db import models
import random
import os


# Create your models here.
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name , ext = os.path.splitext(base_name)
    return name , ext  

def upload_image_path(instance , filename):
    print(instance)
    print(filename)
    new_filename=random.randint(1,4000000)
    name , ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename , ext= ext)

    return "libraryapps/{new_filename}/{final_filename}".format(new_filename=new_filename , final_filename=final_filename)


class Genre(models.Model):
    
    name = models.CharField(
        max_length=200,
        help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)"
        )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class Language(models.Model):
   
    language_name = models.CharField(max_length=200,
                            help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.language_name



class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.CASCADE,null=True ,related_name='author')
    image = models.FileField(upload_to=upload_image_path ,null=True ,blank=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in file.
    description = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    # ManyToManyField used because a genre can contain many books and a Book can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)

    def display_genre(self):
        """Creates a string for the Genre. This is required to display genre in Admin."""
        return ', '.join([genre.name for genre in self.genre.all()[:3]])

    display_genre.short_description = 'Genre'

   

   

    def __str__(self):
        """String for representing the Model object."""
        return '{0}, {1}'.format(self.title,self.description)
       


class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
   

    class Meta:
        ordering = [ 'first_name' , 'last_name']

    

    def __str__(self):
        """String for representing the Model object."""
        return '{0}, {1}'.format(self.first_name,self.last_name)