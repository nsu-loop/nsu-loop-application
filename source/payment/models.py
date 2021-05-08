from django.db import models

# Create your models here.

class Payment(models.Model):
    """
    This class contains the essential fields and behaviors of the data you’re storing. 
	Each model maps to a single database table.
    
    This class is used to create a database table containg those attributes.
    """
    mobile_number = models.CharField(max_length=20)
    transaction_id = models.CharField(max_length=50)
    verified = models.BooleanField(default=False)

    def __str__(self):
        """
		This method return the transaction id.

		:param name: self - used to access the attributes and methods of the class in python
		:param type: reference
		:return: str
		"""
        return f"{self.transaction_id}"