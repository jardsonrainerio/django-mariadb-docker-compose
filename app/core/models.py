from django.db import models


# Create your models here.
class ModelBase(models.Model):
    id = models.AutoField(
        primary_key=True,
        null=False
    )
    active = models.BooleanField(
        null=False,
        default=True
    )
    created_at = models.DateTimeField(
        null=False,
        auto_now_add=True
    )
    modified_at = models.DateTimeField(
        null=False,
        auto_now=True
    )

    class Meta:
        abstract = True
        managed = True


class State(ModelBase):
    name = models.CharField(
        null=False,
        max_length=64,
        unique=True
    )
    abbreviation = models.CharField(
        null=False,
        max_length=2,
        unique=True
    )

    class Meta:
        db_table = 'state'

    def __str__(self):
        return self.name


class City(ModelBase):
    name = models.CharField(
        null=False,
        max_length=64
    )
    state = models.ForeignKey(
        to='State',
        on_delete=models.DO_NOTHING,
        null=False,
        db_column='id_state'
    )

    class Meta:
        db_table = 'city'
        unique_together = [
            ('name', 'state',)
        ]

    def __str__(self):
        return self.name


class Company(ModelBase):
    name = models.CharField(
        null=False,
        max_length=64,
        unique=True
    )
    key = models.CharField(
        null=False,
        max_length=64,
        unique=True
    )
    city = models.ForeignKey(
        to='City',
        on_delete=models.DO_NOTHING,
        null=False,
        db_column='id_city'
    )

    class Meta:
        db_table = 'company'

    def __str__(self):
        return self.name


class Customer(ModelBase):
    class Gender(models.TextChoices):
        FEMALE = 'F', 'Female'
        MALE = 'M', 'Male'

    name = models.CharField(
        null=False,
        max_length=64,
    )
    gender = models.CharField(
        null=False,
        max_length=1,
        choices=Gender.choices
    )

    class Meta:
        db_table = 'customer'

    def __str__(self):
        return self.name


class Service(ModelBase):
    name = models.CharField(
        null=False,
        max_length=64,
        unique=True
    )
    sale_price = models.DecimalField(
        null=False,
        max_digits=16,
        decimal_places=2
    )

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.name


class Sale(ModelBase):
    company = models.ForeignKey(
        to='Company',
        on_delete=models.DO_NOTHING,
        null=False,
        db_column='id_company'
    )
    customer = models.ForeignKey(
        to='Customer',
        on_delete=models.DO_NOTHING,
        null=False,
        db_column='id_customer'
    )
    service = models.ForeignKey(
        to='Service',
        on_delete=models.DO_NOTHING,
        null=False,
        db_column='id_service'
    )

    class Meta:
        db_table = 'sale'

    def __str__(self):
        return "{} - {}".format(self.customer, self.service, )