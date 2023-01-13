from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import models
from django.template.defaultfilters import slugify  # new


class CookieStand(models.Model):
    location = models.CharField(max_length=256)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(default="", null=True, blank=True)
    hourly_sales = models.JSONField(default=list, blank=True)
    minimum_customers_per_hour = models.IntegerField(default=0)
    maximum_customers_per_hour = models.IntegerField(default=0)
    average_cookies_per_sale = models.FloatField(default=0)
    slug = models.SlugField(default="",null=False, unique=True)

    def get_absolute_url(self):
        return reverse("CookieStand_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.location)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.location
