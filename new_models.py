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

class AllTrimImages(models.Model):
    id = models.IntegerField(primary_key=True)
    image2 = models.TextField(blank=True)
    image1 = models.TextField(blank=True)
    synsetid2 = models.FloatField(blank=True, null=True)
    synsetid1 = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'All_trim_images'

class AllYearImages(models.Model):
    id = models.IntegerField(primary_key=True)
    image2 = models.TextField(blank=True)
    image1 = models.TextField(blank=True)
    synsetid2 = models.IntegerField(blank=True, null=True)
    synsetid1 = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'All_year_images'

class Answers1222914(models.Model):
    id = models.IntegerField(primary_key=True)
    different = models.IntegerField(blank=True, null=True)
    difference = models.TextField(blank=True)
    assignmentid = models.TextField(db_column='AssignmentId', blank=True) # Field name made lowercase.
    synsetid2 = models.IntegerField(blank=True, null=True)
    synsetid1 = models.IntegerField(blank=True, null=True)
    hitid = models.TextField(db_column='HITId', blank=True) # Field name made lowercase.
    ground_truth = models.IntegerField(blank=True, null=True)
    approved = models.IntegerField(db_column='Approved', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Answers_1222914'

class Answers1226603(models.Model):
    id = models.IntegerField(primary_key=True)
    different = models.IntegerField(blank=True, null=True)
    difference = models.TextField(blank=True)
    assignmentid = models.TextField(db_column='AssignmentId', blank=True) # Field name made lowercase.
    synsetid2 = models.IntegerField(blank=True, null=True)
    synsetid1 = models.IntegerField(blank=True, null=True)
    hitid = models.TextField(db_column='HITId', blank=True) # Field name made lowercase.
    ground_truth = models.IntegerField(blank=True, null=True)
    approved = models.IntegerField(db_column='Approved', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Answers_1226603'

class Answers1228673(models.Model):
    id = models.IntegerField(primary_key=True)
    different = models.IntegerField(blank=True, null=True)
    difference = models.TextField(blank=True)
    assignmentid = models.TextField(db_column='AssignmentId', blank=True) # Field name made lowercase.
    synsetid2 = models.IntegerField(blank=True, null=True)
    synsetid1 = models.IntegerField(blank=True, null=True)
    hitid = models.TextField(db_column='HITId', blank=True) # Field name made lowercase.
    ground_truth = models.IntegerField(blank=True, null=True)
    approved = models.IntegerField(db_column='Approved', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Answers_1228673'

class Answers1229061(models.Model):
    id = models.IntegerField(primary_key=True)
    ground_both = models.IntegerField(blank=True, null=True)
    difference = models.TextField(blank=True)
    ground_yes = models.IntegerField(blank=True, null=True)
    assignmentid = models.TextField(db_column='AssignmentId', blank=True) # Field name made lowercase.
    workerid = models.TextField(db_column='WorkerId', blank=True) # Field name made lowercase.
    worktime = models.TextField(db_column='WorkTime', blank=True) # Field name made lowercase.
    different = models.IntegerField(blank=True, null=True)
    synsetid1 = models.IntegerField(blank=True, null=True)
    ground_no = models.IntegerField(blank=True, null=True)
    synsetid2 = models.IntegerField(blank=True, null=True)
    hitid = models.TextField(db_column='HITId', blank=True) # Field name made lowercase.
    ground_truth = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'Answers_1229061'

class ClassNegatives(models.Model):
    id = models.IntegerField(primary_key=True)
    difference = models.TextField(blank=True)
    group_id1 = models.IntegerField(blank=True, null=True)
    synsetid2 = models.IntegerField(blank=True, null=True)
    synsetid1 = models.IntegerField(blank=True, null=True)
    group_id2 = models.IntegerField(blank=True, null=True)
    from_tasks = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'Class_negatives'

class NissanYearImages(models.Model):
    id = models.IntegerField(primary_key=True)
    image2 = models.TextField(blank=True)
    image1 = models.TextField(blank=True)
    synsetid2 = models.IntegerField(blank=True, null=True)
    synsetid1 = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'Nissan_year_images'

class Results1222914(models.Model):
    assignmentid = models.CharField(db_column='AssignmentId', primary_key=True, max_length=30) # Field name made lowercase.
    response2 = models.TextField(blank=True)
    response3 = models.TextField(blank=True)
    response0 = models.TextField(blank=True)
    response1 = models.TextField(blank=True)
    synsetid10 = models.IntegerField(blank=True, null=True)
    synsetid11 = models.IntegerField(blank=True, null=True)
    synsetid12 = models.IntegerField(blank=True, null=True)
    synsetid13 = models.IntegerField(blank=True, null=True)
    enough_value1 = models.TextField(blank=True)
    enough_value0 = models.TextField(blank=True)
    enough_value3 = models.TextField(blank=True)
    enough_value2 = models.TextField(blank=True)
    accepttime = models.TextField(db_column='AcceptTime', blank=True) # Field name made lowercase.
    hitid = models.TextField(db_column='HITId', blank=True) # Field name made lowercase.
    enough_value = models.TextField(blank=True)
    rejectiontime = models.TextField(db_column='RejectionTime', blank=True) # Field name made lowercase.
    autoapprovaltime = models.TextField(db_column='AutoApprovalTime', blank=True) # Field name made lowercase.
    yes_value = models.TextField(blank=True)
    worktimeinseconds = models.IntegerField(db_column='WorkTimeInSeconds', blank=True, null=True) # Field name made lowercase.
    assignmentstatus = models.TextField(db_column='AssignmentStatus', blank=True) # Field name made lowercase.
    no_value0 = models.TextField(blank=True)
    unclear_image = models.TextField(blank=True)
    no_value2 = models.TextField(blank=True)
    golden_index = models.IntegerField(blank=True, null=True)
    no_value3 = models.TextField(blank=True)
    yes_value1 = models.TextField(blank=True)
    yes_value0 = models.TextField(blank=True)
    yes_value3 = models.TextField(blank=True)
    yes_value2 = models.TextField(blank=True)
    synsetid21 = models.IntegerField(blank=True, null=True)
    synsetid20 = models.IntegerField(blank=True, null=True)
    synsetid23 = models.IntegerField(blank=True, null=True)
    synsetid22 = models.IntegerField(blank=True, null=True)
    no_value1 = models.TextField(blank=True)
    response = models.TextField(blank=True)
    unclear_image3 = models.TextField(blank=True)
    unclear_image2 = models.TextField(blank=True)
    golden_answer = models.TextField(blank=True)
    unclear_image0 = models.TextField(blank=True)
    unclear_image1 = models.TextField(blank=True)
    synsetid2 = models.IntegerField(blank=True, null=True)
    synsetid1 = models.IntegerField(blank=True, null=True)
    submittime = models.TextField(db_column='SubmitTime', blank=True) # Field name made lowercase.
    workerid = models.TextField(db_column='WorkerId', blank=True) # Field name made lowercase.
    no_value = models.TextField(blank=True)
    approvaltime = models.TextField(db_column='ApprovalTime', blank=True) # Field name made lowercase.
    bumpers = models.TextField(db_column='Bumpers', blank=True) # Field name made lowercase.
    bumpers3 = models.TextField(db_column='Bumpers3', blank=True) # Field name made lowercase.
    headlights3 = models.TextField(db_column='Headlights3', blank=True) # Field name made lowercase.
    fenders3 = models.TextField(db_column='Fenders3', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Results_1222914'

class Results1226603(models.Model):
    assignmentid = models.CharField(db_column='AssignmentId', primary_key=True, max_length=30) # Field name made lowercase.
    response2 = models.TextField(blank=True)
    response3 = models.TextField(blank=True)
    response0 = models.TextField(blank=True)
    response1 = models.TextField(blank=True)
    synsetid10 = models.IntegerField(blank=True, null=True)
    synsetid11 = models.IntegerField(blank=True, null=True)
    synsetid12 = models.IntegerField(blank=True, null=True)
    synsetid13 = models.IntegerField(blank=True, null=True)
    no_value2 = models.TextField(blank=True)
    no_value3 = models.TextField(blank=True)
    no_value0 = models.TextField(blank=True)
    no_value1 = models.TextField(blank=True)
    accepttime = models.TextField(db_column='AcceptTime', blank=True) # Field name made lowercase.
    hitid = models.TextField(db_column='HITId', blank=True) # Field name made lowercase.
    enough_value = models.TextField(blank=True)
    rejectiontime = models.TextField(db_column='RejectionTime', blank=True) # Field name made lowercase.
    autoapprovaltime = models.TextField(db_column='AutoApprovalTime', blank=True) # Field name made lowercase.
    yes_value = models.TextField(blank=True)
    worktimeinseconds = models.TextField(db_column='WorkTimeInSeconds', blank=True) # Field name made lowercase.
    assignmentstatus = models.TextField(db_column='AssignmentStatus', blank=True) # Field name made lowercase.
    unclear_image = models.TextField(blank=True)
    enough_value1 = models.TextField(blank=True)
    golden_index = models.IntegerField(blank=True, null=True)
    enough_value0 = models.TextField(blank=True)
    yes_value1 = models.TextField(blank=True)
    yes_value0 = models.TextField(blank=True)
    yes_value3 = models.TextField(blank=True)
    yes_value2 = models.TextField(blank=True)
    synsetid21 = models.IntegerField(blank=True, null=True)
    enough_value3 = models.TextField(blank=True)
    synsetid23 = models.IntegerField(blank=True, null=True)
    synsetid22 = models.IntegerField(blank=True, null=True)
    enough_value2 = models.TextField(blank=True)
    response = models.TextField(blank=True)
    unclear_image3 = models.TextField(blank=True)
    unclear_image2 = models.TextField(blank=True)
    golden_answer = models.TextField(blank=True)
    unclear_image0 = models.TextField(blank=True)
    unclear_image1 = models.TextField(blank=True)
    synsetid2 = models.IntegerField(blank=True, null=True)
    synsetid1 = models.IntegerField(blank=True, null=True)
    submittime = models.TextField(db_column='SubmitTime', blank=True) # Field name made lowercase.
    workerid = models.TextField(db_column='WorkerId', blank=True) # Field name made lowercase.
    no_value = models.TextField(blank=True)
    synsetid20 = models.IntegerField(blank=True, null=True)
    approvaltime = models.TextField(db_column='ApprovalTime', blank=True) # Field name made lowercase.
    headlights0 = models.TextField(db_column='Headlights0', blank=True) # Field name made lowercase.
    hoods3 = models.TextField(db_column='Hoods3', blank=True) # Field name made lowercase.
    headlights1 = models.TextField(db_column='Headlights1', blank=True) # Field name made lowercase.
    headlights3 = models.TextField(db_column='Headlights3', blank=True) # Field name made lowercase.
    grilles3 = models.TextField(db_column='Grilles3', blank=True) # Field name made lowercase.
    bumpers3 = models.TextField(db_column='Bumpers3', blank=True) # Field name made lowercase.
    tailgates3 = models.TextField(db_column='Tailgates3', blank=True) # Field name made lowercase.
    mirrors3 = models.TextField(db_column='Mirrors3', blank=True) # Field name made lowercase.
    tail_lights3 = models.TextField(db_column='Tail_Lights3', blank=True) # Field name made lowercase.
    trunk_lids1 = models.TextField(db_column='Trunk_Lids1', blank=True) # Field name made lowercase.
    bumpers0 = models.TextField(db_column='Bumpers0', blank=True) # Field name made lowercase.
    headlights2 = models.TextField(db_column='Headlights2', blank=True) # Field name made lowercase.
    tailgates0 = models.TextField(db_column='Tailgates0', blank=True) # Field name made lowercase.
    tailgates2 = models.TextField(db_column='Tailgates2', blank=True) # Field name made lowercase.
    windows2 = models.TextField(db_column='Windows2', blank=True) # Field name made lowercase.
    hoods2 = models.TextField(db_column='Hoods2', blank=True) # Field name made lowercase.
    doors2 = models.TextField(db_column='Doors2', blank=True) # Field name made lowercase.
    grilles2 = models.TextField(db_column='Grilles2', blank=True) # Field name made lowercase.
    bumpers2 = models.TextField(db_column='Bumpers2', blank=True) # Field name made lowercase.
    fenders2 = models.TextField(db_column='Fenders2', blank=True) # Field name made lowercase.
    grilles = models.TextField(db_column='Grilles', blank=True) # Field name made lowercase.
    mirrors0 = models.TextField(db_column='Mirrors0', blank=True) # Field name made lowercase.
    trunk_lids0 = models.TextField(db_column='Trunk_Lids0', blank=True) # Field name made lowercase.
    hoods0 = models.TextField(db_column='Hoods0', blank=True) # Field name made lowercase.
    grilles0 = models.TextField(db_column='Grilles0', blank=True) # Field name made lowercase.
    grilles1 = models.TextField(db_column='Grilles1', blank=True) # Field name made lowercase.
    trunk_lids3 = models.TextField(db_column='Trunk_Lids3', blank=True) # Field name made lowercase.
    bumpers = models.TextField(db_column='Bumpers', blank=True) # Field name made lowercase.
    bumpers1 = models.TextField(db_column='Bumpers1', blank=True) # Field name made lowercase.
    headlights = models.TextField(db_column='Headlights', blank=True) # Field name made lowercase.
    fenders3 = models.TextField(db_column='Fenders3', blank=True) # Field name made lowercase.
    windows0 = models.TextField(db_column='Windows0', blank=True) # Field name made lowercase.
    doors0 = models.TextField(db_column='Doors0', blank=True) # Field name made lowercase.
    fenders0 = models.TextField(db_column='Fenders0', blank=True) # Field name made lowercase.
    mirrors1 = models.TextField(db_column='Mirrors1', blank=True) # Field name made lowercase.
    doors = models.TextField(db_column='Doors', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Results_1226603'

class Results1228673(models.Model):
    assignmentid = models.CharField(db_column='AssignmentId', primary_key=True, max_length=30) # Field name made lowercase.
    response4 = models.TextField(blank=True)
    response2 = models.TextField(blank=True)
    response3 = models.TextField(blank=True)
    response0 = models.TextField(blank=True)
    response1 = models.TextField(blank=True)
    synsetid10 = models.IntegerField(blank=True, null=True)
    synsetid11 = models.IntegerField(blank=True, null=True)
    no_value4 = models.TextField(blank=True)
    synsetid13 = models.IntegerField(blank=True, null=True)
    no_value2 = models.TextField(blank=True)
    no_value3 = models.TextField(blank=True)
    no_value0 = models.TextField(blank=True)
    no_value1 = models.TextField(blank=True)
    golden_no_index = models.IntegerField(blank=True, null=True)
    worktimeinseconds = models.TextField(db_column='WorkTimeInSeconds', blank=True) # Field name made lowercase.
    hitid = models.TextField(db_column='HITId', blank=True) # Field name made lowercase.
    enough_value = models.TextField(blank=True)
    rejectiontime = models.TextField(db_column='RejectionTime', blank=True) # Field name made lowercase.
    autoapprovaltime = models.TextField(db_column='AutoApprovalTime', blank=True) # Field name made lowercase.
    yes_value = models.TextField(blank=True)
    golden_yes_index = models.IntegerField(blank=True, null=True)
    enough_value1 = models.TextField(blank=True)
    enough_value4 = models.TextField(blank=True)
    assignmentstatus = models.TextField(db_column='AssignmentStatus', blank=True) # Field name made lowercase.
    synsetid12 = models.IntegerField(blank=True, null=True)
    unclear_image = models.TextField(blank=True)
    synsetid14 = models.IntegerField(blank=True, null=True)
    enough_value0 = models.TextField(blank=True)
    yes_value1 = models.TextField(blank=True)
    synsetid24 = models.IntegerField(blank=True, null=True)
    yes_value3 = models.TextField(blank=True)
    yes_value2 = models.TextField(blank=True)
    synsetid21 = models.IntegerField(blank=True, null=True)
    synsetid20 = models.IntegerField(blank=True, null=True)
    synsetid23 = models.IntegerField(blank=True, null=True)
    synsetid22 = models.IntegerField(blank=True, null=True)
    enough_value2 = models.TextField(blank=True)
    response = models.TextField(blank=True)
    yes_value0 = models.TextField(blank=True)
    accepttime = models.TextField(db_column='AcceptTime', blank=True) # Field name made lowercase.
    unclear_image4 = models.TextField(blank=True)
    unclear_image2 = models.TextField(blank=True)
    unclear_image3 = models.TextField(blank=True)
    unclear_image0 = models.TextField(blank=True)
    unclear_image1 = models.TextField(blank=True)
    synsetid2 = models.IntegerField(blank=True, null=True)
    synsetid1 = models.IntegerField(blank=True, null=True)
    submittime = models.TextField(db_column='SubmitTime', blank=True) # Field name made lowercase.
    enough_value3 = models.TextField(blank=True)
    workerid = models.TextField(db_column='WorkerId', blank=True) # Field name made lowercase.
    no_value = models.TextField(blank=True)
    yes_value4 = models.TextField(blank=True)
    tailgates = models.TextField(db_column='Tailgates', blank=True) # Field name made lowercase.
    windows4 = models.TextField(db_column='Windows4', blank=True) # Field name made lowercase.
    windows3 = models.TextField(db_column='Windows3', blank=True) # Field name made lowercase.
    mirrors3 = models.TextField(db_column='Mirrors3', blank=True) # Field name made lowercase.
    hoods3 = models.TextField(db_column='Hoods3', blank=True) # Field name made lowercase.
    hoods4 = models.TextField(db_column='Hoods4', blank=True) # Field name made lowercase.
    bumpers = models.TextField(db_column='Bumpers', blank=True) # Field name made lowercase.
    doors4 = models.TextField(db_column='Doors4', blank=True) # Field name made lowercase.
    doors3 = models.TextField(db_column='Doors3', blank=True) # Field name made lowercase.
    exhaust4 = models.TextField(db_column='Exhaust4', blank=True) # Field name made lowercase.
    grilles = models.TextField(db_column='Grilles', blank=True) # Field name made lowercase.
    fenders = models.TextField(db_column='Fenders', blank=True) # Field name made lowercase.
    mirrors = models.TextField(db_column='Mirrors', blank=True) # Field name made lowercase.
    headlights = models.TextField(db_column='Headlights', blank=True) # Field name made lowercase.
    tailgates3 = models.TextField(db_column='Tailgates3', blank=True) # Field name made lowercase.
    tailgates4 = models.TextField(db_column='Tailgates4', blank=True) # Field name made lowercase.
    doors = models.TextField(db_column='Doors', blank=True) # Field name made lowercase.
    hoods = models.TextField(db_column='Hoods', blank=True) # Field name made lowercase.
    headlights4 = models.TextField(db_column='Headlights4', blank=True) # Field name made lowercase.
    exhaust = models.TextField(db_column='Exhaust', blank=True) # Field name made lowercase.
    trunk_lids3 = models.TextField(db_column='Trunk_Lids3', blank=True) # Field name made lowercase.
    trunk_lids4 = models.TextField(db_column='Trunk_Lids4', blank=True) # Field name made lowercase.
    headlights3 = models.TextField(db_column='Headlights3', blank=True) # Field name made lowercase.
    mirrors4 = models.TextField(db_column='Mirrors4', blank=True) # Field name made lowercase.
    tail_lights = models.TextField(db_column='Tail_Lights', blank=True) # Field name made lowercase.
    exhaust3 = models.TextField(db_column='Exhaust3', blank=True) # Field name made lowercase.
    trunk_lids = models.TextField(db_column='Trunk_Lids', blank=True) # Field name made lowercase.
    windows = models.TextField(db_column='Windows', blank=True) # Field name made lowercase.
    tail_lights3 = models.TextField(db_column='Tail_Lights3', blank=True) # Field name made lowercase.
    tail_lights4 = models.TextField(db_column='Tail_Lights4', blank=True) # Field name made lowercase.
    grilles3 = models.TextField(db_column='Grilles3', blank=True) # Field name made lowercase.
    grilles4 = models.TextField(db_column='Grilles4', blank=True) # Field name made lowercase.
    fenders4 = models.TextField(db_column='Fenders4', blank=True) # Field name made lowercase.
    bumpers3 = models.TextField(db_column='Bumpers3', blank=True) # Field name made lowercase.
    bumpers4 = models.TextField(db_column='Bumpers4', blank=True) # Field name made lowercase.
    fenders3 = models.TextField(db_column='Fenders3', blank=True) # Field name made lowercase.
    approvaltime = models.TextField(db_column='ApprovalTime', blank=True) # Field name made lowercase.
    headlights1 = models.TextField(db_column='Headlights1', blank=True) # Field name made lowercase.
    tail_lights2 = models.TextField(db_column='Tail_Lights2', blank=True) # Field name made lowercase.
    grilles1 = models.TextField(db_column='Grilles1', blank=True) # Field name made lowercase.
    grilles2 = models.TextField(db_column='Grilles2', blank=True) # Field name made lowercase.
    bumpers1 = models.TextField(db_column='Bumpers1', blank=True) # Field name made lowercase.
    headlights0 = models.TextField(db_column='Headlights0', blank=True) # Field name made lowercase.
    grilles0 = models.TextField(db_column='Grilles0', blank=True) # Field name made lowercase.
    bumpers0 = models.TextField(db_column='Bumpers0', blank=True) # Field name made lowercase.
    tailgates2 = models.TextField(db_column='Tailgates2', blank=True) # Field name made lowercase.
    windows2 = models.TextField(db_column='Windows2', blank=True) # Field name made lowercase.
    trunk_lids2 = models.TextField(db_column='Trunk_Lids2', blank=True) # Field name made lowercase.
    headlights2 = models.TextField(db_column='Headlights2', blank=True) # Field name made lowercase.
    exhaust2 = models.TextField(db_column='Exhaust2', blank=True) # Field name made lowercase.
    doors2 = models.TextField(db_column='Doors2', blank=True) # Field name made lowercase.
    bumpers2 = models.TextField(db_column='Bumpers2', blank=True) # Field name made lowercase.
    tailgates1 = models.TextField(db_column='Tailgates1', blank=True) # Field name made lowercase.
    windows1 = models.TextField(db_column='Windows1', blank=True) # Field name made lowercase.
    hoods1 = models.TextField(db_column='Hoods1', blank=True) # Field name made lowercase.
    trunk_lids1 = models.TextField(db_column='Trunk_Lids1', blank=True) # Field name made lowercase.
    doors1 = models.TextField(db_column='Doors1', blank=True) # Field name made lowercase.
    tail_lights1 = models.TextField(db_column='Tail_Lights1', blank=True) # Field name made lowercase.
    fenders1 = models.TextField(db_column='Fenders1', blank=True) # Field name made lowercase.
    fenders2 = models.TextField(db_column='Fenders2', blank=True) # Field name made lowercase.
    hoods2 = models.TextField(db_column='Hoods2', blank=True) # Field name made lowercase.
    windows0 = models.TextField(db_column='Windows0', blank=True) # Field name made lowercase.
    hoods0 = models.TextField(db_column='Hoods0', blank=True) # Field name made lowercase.
    doors0 = models.TextField(db_column='Doors0', blank=True) # Field name made lowercase.
    mirrors2 = models.TextField(db_column='Mirrors2', blank=True) # Field name made lowercase.
    tail_lights0 = models.TextField(db_column='Tail_Lights0', blank=True) # Field name made lowercase.
    mirrors0 = models.TextField(db_column='Mirrors0', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Results_1228673'

class YearImages(models.Model):
    id = models.IntegerField(primary_key=True)
    image2 = models.TextField(blank=True)
    image1 = models.TextField(blank=True)
    synsetid2 = models.IntegerField(blank=True, null=True)
    synsetid1 = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'Year_images'

class YearSynsets(models.Model):
    id = models.IntegerField(primary_key=True)
    superset1 = models.IntegerField(blank=True, null=True)
    superset2 = models.IntegerField(blank=True, null=True)
    subset1 = models.IntegerField(blank=True, null=True)
    subset2 = models.IntegerField(blank=True, null=True)
    different = models.IntegerField(blank=True, null=True)
    difference = models.TextField(blank=True)
    merged_dup = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'Year_synsets'

class AllSharedImages(models.Model):
    id = models.IntegerField(primary_key=True)
    syn1_sim = models.FloatField(blank=True, null=True)
    syn2_sim = models.FloatField(blank=True, null=True)
    num_images = models.FloatField(blank=True, null=True)
    synsetid2 = models.FloatField(blank=True, null=True)
    synsetid1 = models.FloatField(blank=True, null=True)
    groupid1 = models.IntegerField(blank=True, null=True)
    groupid2 = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'all_shared_images'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=80)
    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group_id = models.IntegerField()
    permission_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    group_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    permission_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'

class CraigslistCandidates(models.Model):
    synsetid = models.IntegerField(blank=True, null=True)
    image_id = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'craigslist_candidates'

class CraigslistClasses(models.Model):
    posting_id = models.BigIntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    synsetid = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'craigslist_classes'

class CraigslistIms(models.Model):
    posting_id = models.BigIntegerField(blank=True, null=True)
    path = models.CharField(max_length=500, blank=True)
    image_id = models.IntegerField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'craigslist_ims'

class CrawledImages(models.Model):
    synsetid = models.IntegerField(blank=True, null=True)
    path = models.CharField(primary_key=True, max_length=256)
    valid_image = models.IntegerField(blank=True, null=True)
    duplicate = models.IntegerField(blank=True, null=True)
    source_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'crawled_images'

class CrawledSources(models.Model):
    source_id = models.IntegerField(primary_key=True)
    source_name = models.CharField(max_length=256, blank=True)
    class Meta:
        managed = False
        db_table = 'crawled_sources'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user_id = models.IntegerField()
    content_type_id = models.IntegerField(blank=True, null=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta:
        managed = False
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'django_session'

class DuplicateDiff(models.Model):
    id = models.IntegerField(primary_key=True)
    synsetid1 = models.IntegerField()
    synsetid2 = models.IntegerField()
    difference = models.TextField()
    class Meta:
        managed = False
        db_table = 'duplicate_diff'

class DuplicatePairs(models.Model):
    synsetid1 = models.IntegerField()
    synsetid2 = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'duplicate_pairs'

class EdmundExamples(models.Model):
    id = models.IntegerField(primary_key=True)
    synsetid = models.IntegerField(blank=True, null=True)
    old_path = models.CharField(max_length=10000, blank=True)
    edmunds_url = models.CharField(max_length=10000)
    duplicate = models.IntegerField(blank=True, null=True)
    md5 = models.CharField(max_length=10000, blank=True)
    path = models.CharField(max_length=10000, blank=True)
    group_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'edmund_examples'

class FordNegativeExamples(models.Model):
    id = models.IntegerField(primary_key=True)
    example_id = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ford_negative_examples'

class FordPositiveExamples(models.Model):
    id = models.IntegerField(primary_key=True)
    example_id = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ford_positive_examples'

class GroupNames(models.Model):
    id = models.IntegerField(primary_key=True)
    group_id = models.IntegerField(blank=True, null=True)
    group_name = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'group_names'

class GroupsModelOne(models.Model):
    number_1new_group_id = models.IntegerField(db_column='1new_group_id', blank=True, null=True) # Field renamed because it wasn't a valid Python identifier.
    class Meta:
        managed = False
        db_table = 'groups_model_one'

class MaxCraigslitImageGroups(models.Model):
    group_id = models.IntegerField(blank=True, null=True)
    count_distinct_image_id_field = models.BigIntegerField(db_column='count(distinct(image_id))') # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    class Meta:
        managed = False
        db_table = 'max_craigslit_image_groups'

class Md5DuplicatePairs(models.Model):
    synsetid1 = models.IntegerField()
    synsetid2 = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'md5_duplicate_pairs'

class NegativeExamples(models.Model):
    id = models.IntegerField(primary_key=True)
    example_id = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    group_id2 = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'negative_examples'

class NoImagesForGroup(models.Model):
    group_id = models.IntegerField(blank=True, null=True)
    group_name = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'no_images_for_group'

class PairsDupImages(models.Model):
    synsetid1 = models.IntegerField()
    synsetid2 = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'pairs_dup_images'

class PollsChoice(models.Model):
    id = models.IntegerField(primary_key=True)
    poll_id = models.IntegerField()
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'polls_choice'

class PollsPoll(models.Model):
    id = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'polls_poll'

class PositiveExamples(models.Model):
    id = models.IntegerField(primary_key=True)
    example_id = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'positive_examples'

class SharedImages(models.Model):
    id = models.IntegerField(primary_key=True)
    syn1_sim = models.FloatField(blank=True, null=True)
    syn2_sim = models.FloatField(blank=True, null=True)
    num_images = models.FloatField(blank=True, null=True)
    synsetid2 = models.FloatField(blank=True, null=True)
    synsetid1 = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'shared_images'

class SingletonGroups(models.Model):
    synsetid = models.IntegerField()
    number_1new_group_id = models.IntegerField(db_column='1new_group_id', blank=True, null=True) # Field renamed because it wasn't a valid Python identifier.
    class Meta:
        managed = False
        db_table = 'singleton_groups'

class SmallCraigslistClasses(models.Model):
    posting_id = models.BigIntegerField(blank=True, null=True)
    synsetid = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'small_craigslist_classes'

class SmallGroupNames(models.Model):
    id = models.IntegerField(primary_key=True)
    group_id = models.IntegerField(blank=True, null=True)
    group_name = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'small_group_names'

class Synsets(models.Model):
    synsetid = models.IntegerField(primary_key=True)
    make = models.CharField(max_length=10000)
    model = models.CharField(max_length=10000)
    year = models.IntegerField()
    trim = models.CharField(max_length=10000, blank=True)
    doors = models.CharField(max_length=10000, blank=True)
    duplicate = models.IntegerField(blank=True, null=True)
    merged_trim = models.IntegerField(blank=True, null=True)
    superset = models.IntegerField(blank=True, null=True)
    has_subset = models.IntegerField(blank=True, null=True)
    md5_duplicate = models.IntegerField(blank=True, null=True)
    shared_duplicate = models.IntegerField(blank=True, null=True)
    merged_shared = models.IntegerField(blank=True, null=True)
    merged_year = models.IntegerField(blank=True, null=True)
    year_superset = models.IntegerField(blank=True, null=True)
    has_year_subset = models.IntegerField(blank=True, null=True)
    old_group_id = models.IntegerField(blank=True, null=True)
    new_group_id = models.IntegerField(blank=True, null=True)
    number_1new_group_id = models.IntegerField(db_column='1new_group_id', blank=True, null=True) # Field renamed because it wasn't a valid Python identifier.
    number_2new_group_id = models.IntegerField(db_column='2new_group_id', blank=True, null=True) # Field renamed because it wasn't a valid Python identifier.
    ignore_group = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'synsets'

class SynsetsMerged(models.Model):
    synsetid = models.IntegerField(primary_key=True)
    deduped = models.IntegerField(blank=True, null=True)
    crawled = models.IntegerField(blank=True, null=True)
    crawled_path = models.CharField(max_length=256, blank=True)
    synset_name = models.CharField(max_length=128)
    class Meta:
        managed = False
        db_table = 'synsets_merged'

class TestNegativeExamples(models.Model):
    id = models.IntegerField(primary_key=True)
    example_id = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'test_negative_examples'

class TestPositiveExamples(models.Model):
    id = models.IntegerField(primary_key=True)
    example_id = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'test_positive_examples'

class TrimDiff(models.Model):
    id = models.IntegerField(primary_key=True)
    difference = models.TextField(blank=True)
    synsetid2 = models.IntegerField(blank=True, null=True)
    synsetid1 = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'trim_diff'

class TrimGroups(models.Model):
    pair_id = models.IntegerField(primary_key=True)
    subset_id = models.IntegerField()
    superset_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'trim_groups'

class Workers(models.Model):
    id = models.IntegerField(primary_key=True)
    worker_id = models.TextField()
    worker_time = models.IntegerField()
    hitid = models.TextField(blank=True)
    response = models.CharField(max_length=10000)
    class Meta:
        managed = False
        db_table = 'workers'

class YearGroundNo(models.Model):
    id = models.IntegerField(primary_key=True)
    synsetid1 = models.IntegerField()
    synsetid2 = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'year_ground_no'

class YearGroups(models.Model):
    pair_id = models.IntegerField(primary_key=True)
    subset_id = models.IntegerField()
    superset_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'year_groups'

class YearsCheckNo(models.Model):
    synsetid1 = models.IntegerField()
    synsetid2 = models.IntegerField()
    different = models.IntegerField()
    difference = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'years_check_no'

