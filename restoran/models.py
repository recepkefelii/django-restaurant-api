from django.db import models
from projectBackend.base import BaseModel


class restaurant(BaseModel):
    name = models.CharField(max_length=20)
    person_count = models.IntegerField(default=1)
    sub = models.BooleanField(default=False)
    
    
    def __str__(self) -> str:
        return self.name
    
    



class Menu(BaseModel):
    name = models.CharField(max_length=20)
    restoran = models.ForeignKey(restaurant,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
      
    



class Food(BaseModel):
    class Category(models.TextChoices):
        FRESHMAN = 'DRINKS', ('Drinks')
        SOPHOMORE = 'SOUPS', ('Soups')
        JUNIOR = 'SALADS', ('Salads')
        SENIOR = 'SWEET', ('Sweet')
        GRADUATE = 'BREAKFAST', ('Breakfast')
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    description = models.CharField(max_length=50)
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE,related_name='Menu')
    category = models.CharField(choices=Category.choices,max_length=20)

    def __str__(self) -> str:
        return self.name



