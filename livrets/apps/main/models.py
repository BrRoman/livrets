""" apps/main/models.py """

from django.db import models
from django.db.models.fields import CharField, TextField


class Day(models.Model):
    """ Class Day. """
    ref = models.CharField(
        max_length=50,
        db_column='Ref',
    )
    day = models.CharField(
        max_length=255,
        db_column='Day',
    )
    rank = models.CharField(
        max_length=255,
        choices=[
            ('Solennité', 'Solennité'),
            ('Fête', 'Fête'),
            ('Mémoire majeure', 'Mémoire majeure'),
            ('Mémoire mineure', 'Mémoire mineure'),
        ],
        db_column='Rang',
    )
    precedence = models.IntegerField(
        choices=[
            ('10', 10),
            ('20', 20),
            ('30', 30),
            ('40', 40),
            ('50', 50),
            ('60', 60),
            ('70', 70),
            ('80', 80),
            ('90', 90),
            ('100', 100),
            ('110', 110),
            ('120', 120),
            ('130', 130),
        ],
        db_column='Precedence',
    )
    tierce = CharField(
        max_length=255,
        db_column='Tierce',
    )
    oraisons_mg = CharField(
        max_length=25,
        db_column='Oraisons_MG',
    )
    readings = models.BooleanField(
        db_column='Lect_propres',
    )
    readings_cycle = models.IntegerField(
        choices=[
            ('1', 1),
            ('2', 2),
            ('3', 3),
            ('6', 6),
        ],
        db_column='Lect_cycle',
    )
    preface = CharField(
        max_length=25,
        db_column=('Pref'),
    )
    preface_name_la = TextField(
        db_column='Pref_name_la',
    )
    preface_name_fr = TextField(
        db_column='Pref_name_fr',
    )
    sequence = CharField(
        max_length=255,
        db_column='Sequence',
    )

    class Meta:
        managed = False
        db_table = 'Days'

    def __str__(self):
        return self.ref
