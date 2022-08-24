"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Contact(models.Model):
    ballot_id = models.CharField(max_length=100)
    contest_id = models.CharField(max_length=100)
    selection_id = models.CharField(max_length=100)
    tally = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Spoiled(models.Model):
    ballot_id = models.CharField(max_length=500, blank=True, null=True)
    contest_id = models.CharField(max_length=500, blank=True, null=True)
    selection_id = models.CharField(max_length=500, blank=True, null=True)
    tally = models.CharField(max_length=500, blank=True, null=True)
    ledger_start_transaction_id = models.BigIntegerField()
    ledger_end_transaction_id = models.BigIntegerField(blank=True, null=True)
    ledger_start_sequence_number = models.BigIntegerField()
    ledger_end_sequence_number = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spoiled'


class Submitted(models.Model):
    ballot_id = models.CharField(max_length=500, blank=True, null=True)
    style_id = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=500, blank=True, null=True)
    timestamp = models.CharField(max_length=500, blank=True, null=True)
    ledger_start_transaction_id = models.BigIntegerField()
    ledger_end_transaction_id = models.BigIntegerField(blank=True, null=True)
    ledger_start_sequence_number = models.BigIntegerField()
    ledger_end_sequence_number = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'submitted'
