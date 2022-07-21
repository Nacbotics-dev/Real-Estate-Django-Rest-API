import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


def property_directory_path(instance, filename):
    return 'PROPERTY_IMAGES/{0}/{1}'.format(instance.property_id,filename)

def property_directory_path_for_Images(instance, filename):
    return 'PROPERTY_IMAGES/{0}/{1}'.format(instance.property.property_id,filename)



class Location(models.Model):
    location = models.CharField(blank=False,max_length=100,unique=True,primary_key=True)

    def __str__(self) -> str:
        return str(self.location)


class Property(models.Model):

    PROPERTY_TYPE = [
            ('Landed',"LANDED"),
            ('House',"HOUSE"),
            ]

    DEAL_TYPE = [
            ("SALE","SALE"),
            ("RENT","RENT"),
            ("LEASE","LEASE"),
            ]
        
    
    property_id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False, unique=True)
    title = models.CharField(blank=False,max_length=100,unique=False)
    property_image = models.ImageField(upload_to = property_directory_path,blank=True)
    location =  models.ForeignKey(Location, on_delete=models.CASCADE,null=False,blank=False)
    address = models.CharField(blank=False,max_length=100,unique=False)
    price = models.BigIntegerField(blank=False)
    dimension = models.IntegerField(blank=False) # by square feet
    no_bedrooms = models.IntegerField(blank=True,default=0)
    no_bathrooms = models.IntegerField(blank=True,default=0)
    description = models.CharField(blank=False,max_length=250)
    details = models.TextField()
    featured = models.BooleanField(default=False)
    property_type = models.CharField(max_length=10,choices=PROPERTY_TYPE,default="Landed")
    deal_type = models.CharField(max_length=10,choices=DEAL_TYPE,default="SALE")
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = _('Property')
        verbose_name_plural = _('Properties')



    def __str__(self) -> str:
        return str(self.property_id)


class Images(models.Model):
    property = models.ForeignKey(Property,on_delete=models.CASCADE)
    images = models.ImageField(upload_to=property_directory_path_for_Images,verbose_name='Image')

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')


    def __str__(self) -> str:
        return str(self.property)
