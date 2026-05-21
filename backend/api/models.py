from django.db import models


class ApiDynasty(models.Model):
    id = models.BigAutoField(primary_key=True)
    did = models.IntegerField()
    dname = models.CharField(max_length=45)

    class Meta:
        db_table = 'api_dynasty'


class ApiProvince(models.Model):
    id = models.BigAutoField(primary_key=True)
    pname = models.CharField(max_length=45)
    sid = models.IntegerField()

    class Meta:
        db_table = 'api_province'


class ApiScenery(models.Model):
    id = models.BigAutoField(primary_key=True)
    sid = models.IntegerField()
    pid = models.IntegerField()
    did = models.IntegerField()
    sname = models.CharField(max_length=45)
    label = models.IntegerField()
    introduction = models.CharField(max_length=1000)
    category = models.IntegerField()

    class Meta:
        db_table = 'api_scenery'


# ---------------- 系统表只做映射：managed = False ----------------

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


# ---------------- 你的数据表模型 ----------------

class Dynasty(models.Model):
    did = models.IntegerField(primary_key=True)
    dname = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'dynasty'


class Province(models.Model):
    pid = models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'province'


class Scenery(models.Model):
    sid = models.IntegerField(primary_key=True)
    sname = models.CharField(max_length=45, blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)
    did = models.IntegerField()
    label = models.IntegerField(blank=True, null=True)
    introduction = models.CharField(max_length=1000, blank=True, null=True)
    category = models.CharField(max_length=45, blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'scenery'
        unique_together = (('sid', 'did'),)


class key(models.Model):
    kid = models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'key'  # 重命名避免冲突


class Category(models.Model):
    cid = models.IntegerField(primary_key=True)
    cname = models.CharField(max_length=255)

    class Meta:
        db_table = 'category'


class Details(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField(blank=True, null=True)
    number = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'details'


class Introduction(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField(blank=True, null=True)
    number = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    dynasty = models.TextField(blank=True, null=True)
    did = models.IntegerField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    public_time = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    district = models.TextField(blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)
    protection_department = models.TextField(blank=True, null=True)
    origin = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'introduction'


class Users(models.Model):
    username = models.CharField(primary_key=True, max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    like = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        db_table = 'Users'
