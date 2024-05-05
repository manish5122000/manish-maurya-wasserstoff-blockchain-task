from django.db import models

# Create your models here.

class LockedTokenModel(models.Model):
    token_address = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=18, decimal_places=2)
   
    target_address = models.CharField(max_length=255)

    def __str__(self):
        return f"LockedTokens {self.id}"
    def __str__(self):
        return f"{self.sender} - {self.amount} {self.token_address}"
    
class managerModel(models.Model):
    manager_address = models.CharField(max_length=50)
    

    











