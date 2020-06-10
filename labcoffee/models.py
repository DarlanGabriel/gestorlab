from django.db import models


class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.first_name} {self.last_name}'


class Presentation(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(max_length=500, help_text='Enter a brief description of the presentation')
    start_date = models.DateTimeField()

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.title} - {self.author}'


