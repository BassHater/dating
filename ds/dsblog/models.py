from django.db import models
from datetime import date
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    """Category"""
    name = models.CharField("Category", max_length=150)
    description = models.TextField("Category Description")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Tags(models.Model):
    """Category"""
    name = models.CharField("Tag", max_length=150)
    description = models.TextField("Tag Description")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

class Page(models.Model):
    """PageBlog"""
    PageTitle = models.CharField(max_length=250, unique=true)
    PageSlug = models.CharField(max_length=120)
    PageMetaKeywords = models.ForeignKey(max_length=120)
    PageMetaDescription = models.TextField("Description")
    FeaturedImage = models.ImageField("FeaturedImage", upload_to="movies/")
    CreatedOn = models.DateField("Created on", default=datetime.now)
    LastEdited = models.DateField("Created on", default=datetime.now)
    country = models.CharField("Страна", max_length=30)
    directors = models.ManyToManyField(Actor, verbose_name="режиссер", related_name="film_director")
    actors = models.ManyToManyField(Actor, verbose_name="актеры", related_name="film_actor")
    genres = models.ManyToManyField(Genre, verbose_name="жанры")
    world_premiere = models.DateField("Примьера в мире", default=date.today)
    budget = models.PositiveIntegerField("Бюджет", default=0,
                                         help_text="указывать сумму в долларах")
    fees_in_usa = models.PositiveIntegerField(
        "Сборы в США", default=0, help_text="указывать сумму в долларах"
    )
    fess_in_world = models.PositiveIntegerField(
        "Сборы в мире", default=0, help_text="указывать сумму в долларах"
    )
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True
    )
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.url})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class Page(models.Model):
    PageTitle = models.CharField(max_length=250, unique=true)
    PageSlug = models.CharField(max_length=120)
    PageMetaKeywords = models.ForeignKey(max_length=120)
