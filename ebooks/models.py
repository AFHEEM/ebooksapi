from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Ebook(models.Model):
    """
    Ebook database table
    """
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    publication_date = models.DateField()

    def __str__(self):
        """
        Represents the database objects display name
        :return:
        """
        return self.title


class Review(models.Model):
    """
    Review an Ebook
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    review_author = models.CharField(max_length=8, blank=True, null=True)
    review = models.TextField(blank=True, null=True)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),
                                                     MaxValueValidator(5)])
    ebook = models.ForeignKey(Ebook,
                              on_delete=models.CASCADE,
                              related_name='reviews')

    def __str__(self):
        """
        Review model representation
        :return:
        """
        return str(self.rating)
