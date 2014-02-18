from django.db import models
import ast, re

def list_to_str(l):

    r = ''
    for i in l:
        r = r + i + ','

    return r[:-1]

class ListField(models.TextField):
    __metaclass__ = models.SubfieldBase
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        if value.find('[') == -1:
            return re.split('\s*,\s*', value)

        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value
        return unicode(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)


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
    inventory_type = models.CharField('Inventory Type',
                                      max_length=64,
                                      choices=TYPE,
                                      default='NEW',
                                      db_index=True)
    year = models.IntegerField('Model Year', db_index=True)
    brand = models.CharField('Brand', max_length=64, default="BMW")
    model = models.CharField('Model', max_length=64, db_index=True)
    vin = models.CharField('VIN', max_length=64, db_index=True, unique=True)
    serial = models.CharField('Serial#', max_length=64, db_index=True)
    stock = models.CharField('Stock#', max_length=64, db_index=True)
    exterior = models.CharField('Exterior Color', max_length=64, db_index=True)
    interior = models.CharField('Interior Color', max_length=64, db_index=True)
    transmission = models.CharField('Transmission Type',
                                    max_length=64, 
                                    choices=TRANSMISSION,
                                    default='A',
                                    db_index=True)
    options = ListField('Options', max_length=10000)
    miles = models.IntegerField('Milage', db_index=True)
    retail = models.DecimalField('Retail Price',
                                 max_digits=10, 
                                 decimal_places=2,db_index=True)
    invoice = models.DecimalField('Invoice Price',
                                  max_digits=10, 
                                  decimal_places=2,
                                  blank=True,
                                  null=True,
                                  db_index=True)
    in_date = models.DateField('In Date', db_index=True)
    detail = models.CharField('Detail',
                              max_length=1000000, 
                              blank=True,
                              null=True)
    

    def __unicode__(self):
        return self.description()

    def description(self):
        return str(self.year) + " " + self.brand + " " + self.model

    def configuration(self):    
        return self.exterior + '/' + self.interior + '/' + list_to_str(self.options)
