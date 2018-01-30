# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals
from django.db import models

class Bboxes(models.Model):
    bbox_id=models.IntegerField(primary_key=True)   
    assignid=models.IntegerField(null=False)   
    synsetid =models.IntegerField(null=False)    
    imageid  =models.IntegerField(null=False)   
    big_enough =models.IntegerField(null=False)   
    new_big_enough =models.IntegerField(null=False)   
    group_id=models.IntegerField(blank=True, null=True)
    make=models.CharField(max_length=10000)
    model=models.CharField(max_length=10000)
    submodel=models.CharField(max_length=10000)

class Cur_state(models.Model):
    bbox=models.ForeignKey(Bboxes)
    box_selected=models.BooleanField(default=0)
    box_done=models.BooleanField(default=0)
    box_good=models.BooleanField(default=0)
    ground_truth=models.BooleanField(default=0)
    user=models.CharField(max_length=10000)
    date_selected=models.DateTimeField(blank=True)

class Synsets(models.Model):
    synsetid = models.IntegerField(primary_key=True)
    make = models.CharField(max_length=10000)
    model = models.CharField(max_length=10000)
    year = models.IntegerField()
    trim = models.CharField(max_length=10000, blank=True)
    doors = models.CharField(max_length=10000, blank=True)
    ignore_group = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'synsets'
        permissions=('')

class EdmundExamples(models.Model):
    id = models.IntegerField(primary_key=True)
    synsetid = models.ForeignKey(Synsets)
    #edmunds_url = models.CharField(max_length=10000)
    path = models.CharField(max_length=10000, blank=True)
    group_id = models.IntegerField(blank=True, null=True)
    viewpoint=models.CharField(max_length=32,null=True)
    class Meta:
        managed = False
        db_table = 'edmund_examples'
        permissions=('')


class PositiveExamples(models.Model):
    id = models.IntegerField(primary_key=True)
    example_id =models.ForeignKey(EdmundExamples)
    group_id = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'positive_examples'
        permissions=('')

class GroupNames(models.Model):
    id = models.IntegerField(primary_key=True)
    group_id = models.IntegerField(blank=True, null=True)
    group_name = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'group_names'
        permissions=('')
