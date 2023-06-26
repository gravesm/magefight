import random

from django.db import models


class Spell(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Mage(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    spells = models.ManyToManyField(Spell, blank=True)

    def __str__(self):
        return self.name


class Fight(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    mages = models.ManyToManyField(Mage, related_name="fights")
    winner = models.ForeignKey(Mage, on_delete=models.CASCADE, editable=False, null=True)
