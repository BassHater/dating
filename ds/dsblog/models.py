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
    PageTitle = models.CharField(max_length=250, null=False)
    PageMetaKeywords = models.ForeignKey(max_length=120, null=False)
    PageMetaDescription = models.TextField("Description", null=False)
    FeaturedImage = models.ImageField("FeaturedImage", upload_to="movies/")
    CreatedOn = models.DateField("Created on", default=datetime.now, null=False)
    LastEdited = models.DateField("Created on", default=datetime.now, null=False)
    Category = models.ForeignKey(
        Category, verbose_name="Category", on_delete=models.SET_NULL, null=True
    )
    IsDraft = models.BooleanField("Draft", default=False)
    IsVisible = models.BooleanField("Draft", default=False)

    PageSlug = models.SlugField("Page Slug", max_length=130, unique=True, null=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.url})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"


