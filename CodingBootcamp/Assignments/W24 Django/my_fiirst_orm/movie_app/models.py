from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateTimeField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __repr__(self):
    #     return "Title: {self.title}"
    # to show the title when using Movie.objects.first() and make sure you restart your shell to have it updated

    # def __str__(self):
    #     return f"<Movie object: {self.title} ({self.id})>"
    
    # def __str__(self):
    #     return f"{self.title}"


# newly_created_movie = Movie.objects.create(title="The Princess Bride",description="the best movie ever",release_date="1987-09-25",duration=98)
# print(newly_created_movie.id)	# view the new movie's id

# newly_created_movie = Movie(title="The Princess Bride",description="the best movie ever",release_date="1987-09-25",duration=98)
# newly_created_movie.save()

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)