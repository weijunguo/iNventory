from django.db import models

    
class SalesPerson(models.Model):
    name = models.CharField(max_length=200)

class Vehicle(models.Model):
    STATUS = (
        ('RC', 'Reconciled'),
        ('RT', 'Retail'),
        )
    
    TRANSMISSION = ( 
        ('A', 'Automatic'),
        ('M', 'Manual'),
        ('DCT', 'Dual-clutch transimission')
        )

    TYPE = (
        ('CPO', 'Certified Pre-owned'),
        ('NPO', 'Non-certified Pre-owned'),
        ('NEW', 'Brand New')
        )
    

    salesperson = models.ForeignKey(SalesPerson, 
                                    blank=True, 
                                    null=True,
                                    db_index=True)
    status = models.CharField(max_length=64, 
                              choices=STATUS,
                              default='RT',
                              db_index=True)
    inventory_type = models.CharField(max_length=64,
                                      choices=TYPE,
                                      default='NEW',
                                      db_index=True)
    year = models.IntegerField(db_index=True)
    model = models.CharField(max_length=64, db_index=True)
    vin = models.CharField(max_length=64, db_index=True)
    serial = models.CharField(max_length=64, db_index=True)
    stock = models.CharField(max_length=64, db_index=True)
    exterior = models.CharField(max_length=64, db_index=True)
    interior = models.CharField(max_length=64, db_index=True)
    transmission = models.CharField(max_length=64, 
                                    choices=TRANSMISSION,
                                    default='A',
                                    db_index=True)
    options = models.CharField(max_length=10000)
    miles = models.IntegerField(db_index=True)
    retail = models.DecimalField(max_digits=10, 
                                 decimal_places=2,db_index=True)
    invoice = models.DecimalField(max_digits=10, 
                                  decimal_places=2,
                                  blank=True,
                                  null=True,
                                  db_index=True)
    in_date = models.DateField(db_index=True)
    detail = models.CharField(max_length=1000000, 
                              blank=True,
                              null=True)


# Create your models here.
