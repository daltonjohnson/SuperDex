from django.db import models

# Create your models here.

class Pokemon(models.Model):
	name = models.CharField(max_length=50)
	nickname = models.CharField(max_length=50)
	number = models.IntegerField(primary_key=True)
	imageurl = models.URLField
	poke_type = models.ForeignKey(Poke_type)
	genderratio = models.CharField(max_length=30)
	catchrate = models.CharField(max_length=30)
	egggroups = models.CharField(max_length=30)
	height_ft = models.CharField(max_length=20)
	height_m = models.CharField(max_length=20)
	weight_lbs = models.CharField(max_length=20)
	weight_kg = models.CharField(max_length=20)
	evhp = models.IntegerField
	evattack = models.IntegerField
	evdefense = models.IntegerField
	evspattack = models.IntegerField
	evdefense = models.IntegerField
	evspeed = models.IntegerField
	basefriendship = models.IntegerField
	basehp = models.IntegerField
	baseattack = models.IntegerField
	basedefense = models.IntegerField
	basespattack = models.IntegerField
	basespdefense = models.IntegerField
	basespeed = models.IntegerField
	basetotal models.IntegerField
	def __str__(self):
		return self.name

class Ability(models.Model):
	ability_id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length = 20)
	description = models.CharField(max_length=200)
	def __str__(self):
		return self.name

class has_ability(models.Model):
	ID = models.ForeignKey()