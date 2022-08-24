# Customization:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class MssqlDroppedledgerhistoryMssqlLedgerhistoryfor1525580473452D2D6459434E29Afb1E24552764A29(models.Model):
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
        db_table = 'MSSQL_DroppedLedgerHistory_MSSQL_LedgerHistoryFor_1525580473_452D2D6459434E29AFB1E24552764A29'


class MssqlDroppedledgertableSpoiledB9A9C0Da92D34877B76Bddd1Ceae2B8C(models.Model):
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
        db_table = 'MSSQL_DroppedLedgerTable_spoiled_B9A9C0DA92D34877B76BDDD1CEAE2B8C'


class MssqlLedgerhistoryfor1573580644(models.Model):
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
        db_table = 'MSSQL_LedgerHistoryFor_1573580644'


class MssqlLedgerhistoryfor1621580815(models.Model):
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
        db_table = 'MSSQL_LedgerHistoryFor_1621580815'


class MssqlLedgerhistoryfor1669580986(models.Model):
    id = models.IntegerField()
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()
    ledger_start_transaction_id = models.BigIntegerField()
    ledger_end_transaction_id = models.BigIntegerField(blank=True, null=True)
    ledger_start_sequence_number = models.BigIntegerField()
    ledger_end_sequence_number = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSSQL_LedgerHistoryFor_1669580986'


class MssqlLedgerhistoryfor1733581214(models.Model):
    id = models.IntegerField()
    mssql_droppedledgercolumn_name_106f613641e943d3b57b2e847021fd70 = models.CharField(db_column='MSSQL_DroppedLedgerColumn_name_106F613641E943D3B57B2E847021FD70', max_length=100, blank=True, null=True)  # Field name made lowercase.
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    ledger_start_transaction_id = models.BigIntegerField()
    ledger_end_transaction_id = models.BigIntegerField(blank=True, null=True)
    ledger_start_sequence_number = models.BigIntegerField()
    ledger_end_sequence_number = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSSQL_LedgerHistoryFor_1733581214'


class MssqlLedgerhistoryfor178099675(models.Model):
    id = models.IntegerField()
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()
    ledger_start_transaction_id = models.BigIntegerField()
    ledger_end_transaction_id = models.BigIntegerField(blank=True, null=True)
    ledger_start_sequence_number = models.BigIntegerField()
    ledger_end_sequence_number = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSSQL_LedgerHistoryFor_178099675'


class MssqlLedgerhistoryfor1797581442(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)
    ledger_start_transaction_id = models.BigIntegerField()
    ledger_end_transaction_id = models.BigIntegerField(blank=True, null=True)
    ledger_start_sequence_number = models.BigIntegerField()
    ledger_end_sequence_number = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSSQL_LedgerHistoryFor_1797581442'


class MssqlLedgerhistoryfor1861581670(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=150)
    ledger_start_transaction_id = models.BigIntegerField()
    ledger_end_transaction_id = models.BigIntegerField(blank=True, null=True)
    ledger_start_sequence_number = models.BigIntegerField()
    ledger_end_sequence_number = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSSQL_LedgerHistoryFor_1861581670'


class MssqlLedgerhistoryfor1941581955(models.Model):
    id = models.IntegerField()
    group_id = models.IntegerField()
    permission_id = models.IntegerField()
    ledger_start_transaction_id = models.BigIntegerField()
    ledger_end_transaction_id = models.BigIntegerField(blank=True, null=True)
    ledger_start_sequence_number = models.BigIntegerField()
    ledger_end_sequence_number = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSSQL_LedgerHistoryFor_1941581955'


class MssqlLedgerhistoryfor2005582183(models.Model):
    id = models.IntegerField()
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    ledger_start_transaction_id = models.BigIntegerField()
    ledger_end_transaction_id = models.BigIntegerField(blank=True, null=True)
    ledger_start_sequence_number = models.BigIntegerField()
    ledger_end_sequence_number = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSSQL_LedgerHistoryFor_2005582183'


class MssqlLedgerhistoryfor2085582468(models.Model):
    id = models.IntegerField()
    user_id = models.IntegerField()
    group_id = models.IntegerField()
    ledger_start_transaction_id = models.BigIntegerField()
    ledger_end_transaction_id = models.BigIntegerField(blank=True, null=True)
    ledger_start_sequence_number = models.BigIntegerField()
    ledger_end_sequence_number = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSSQL_LedgerHistoryFor_2085582468'


class MssqlLedgerhistoryfor2099048(models.Model):
    id = models.IntegerField()
    user_id = models.IntegerField()
    permission_id = models.IntegerField()
    ledger_start_transaction_id = models.BigIntegerField()
    ledger_end_transaction_id = models.BigIntegerField(blank=True, null=True)
    ledger_start_sequence_number = models.BigIntegerField()
    ledger_end_sequence_number = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSSQL_LedgerHistoryFor_2099048'


class MssqlLedgerhistoryfor322100188(models.Model):
    session_key = models.CharField(max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    ledger_start_transaction_id = models.BigIntegerField()
    ledger_end_transaction_id = models.BigIntegerField(blank=True, null=True)
    ledger_start_sequence_number = models.BigIntegerField()
    ledger_end_sequence_number = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSSQL_LedgerHistoryFor_322100188'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)
    ledger_start_transaction_id = models.BigIntegerField()
    ledger_end_transaction_id = models.BigIntegerField(blank=True, null=True)
    ledger_start_sequence_number = models.BigIntegerField()
    ledger_end_sequence_number = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
    ledger_start_transaction_id = models.BigIntegerField()
    ledger_end_transaction_id = models.BigIntegerField(blank=True, null=True)
    ledger_start_sequence_number = models.BigIntegerField()
    ledger_end_sequence_number = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    ledger_start_transaction_id = models.BigIntegerField()
    ledger_end_transaction_id = models.BigIntegerField(blank=True, null=True)
    ledger_start_sequence_number = models.BigIntegerField()
    ledger_end_sequence_number = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    ledger_start_transaction_id = models.BigIntegerField()
    ledger_end_transaction_id = models.BigIntegerField(blank=True, null=True)
    ledger_start_sequence_number = models.BigIntegerField()
    ledger_end_sequence_number = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    ledger_start_transaction_id = models.BigIntegerField()
    ledger_end_transaction_id = models.BigIntegerField(blank=True, null=True)
    ledger_start_sequence_number = models.BigIntegerField()
    ledger_end_sequence_number = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
    ledger_start_transaction_id = models.BigIntegerField()
    ledger_end_transaction_id = models.BigIntegerField(blank=True, null=True)
    ledger_start_sequence_number = models.BigIntegerField()
    ledger_end_sequence_number = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    ledger_start_transaction_id = models.BigIntegerField()
    ledger_end_transaction_id = models.BigIntegerField(blank=True, null=True)
    ledger_start_sequence_number = models.BigIntegerField()
    ledger_end_sequence_number = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    mssql_droppedledgercolumn_name_106f613641e943d3b57b2e847021fd70 = models.CharField(db_column='MSSQL_DroppedLedgerColumn_name_106F613641E943D3B57B2E847021FD70', max_length=100, blank=True, null=True)  # Field name made lowercase.
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    ledger_start_transaction_id = models.BigIntegerField()
    ledger_end_transaction_id = models.BigIntegerField(blank=True, null=True)
    ledger_start_sequence_number = models.BigIntegerField()
    ledger_end_sequence_number = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()
    ledger_start_transaction_id = models.BigIntegerField()
    ledger_end_transaction_id = models.BigIntegerField(blank=True, null=True)
    ledger_start_sequence_number = models.BigIntegerField()
    ledger_end_sequence_number = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    ledger_start_transaction_id = models.BigIntegerField()
    ledger_end_transaction_id = models.BigIntegerField(blank=True, null=True)
    ledger_start_sequence_number = models.BigIntegerField()
    ledger_end_sequence_number = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_session'


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
