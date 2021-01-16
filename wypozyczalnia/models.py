from django.db import models


class FuelType(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'fuel_type'

    def publish(self):
        self.save()

    def __str__(self):
        return self.name


class Engine(models.Model):
    name = models.CharField(max_length=30)
    power = models.FloatField()
    consumation = models.FloatField()
    fuel_type = models.ForeignKey(FuelType, on_delete=models.CASCADE, related_name='engines')

    class Meta:
        db_table = 'engine'

    def publish(self):
        self.save()

    def __str__(self):
        return f'{self.name} | {self.power} KS - {self.consumation} l '


class Model(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'model'

    def publish(self):
        self.save()

    def __str__(self):
        return self.name


class AditionalEquipment(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'aditional_equipment'

    def publish(self):
        self.save()

    def __str__(self):
        return self.name


class Car(models.Model):
    nazwa = models.CharField(max_length=20)
    rok_produkcji = models.IntegerField()
    cena_za_godzine = models.IntegerField()
    dostepnosc = models.BooleanField(default=True)
    klimatyzacja = models.BooleanField(default=True)
    ilosc_drzwi = models.IntegerField()
    ocena = models.FloatField(default=0)
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='cars', null=True)
    silnik = models.ForeignKey(Engine, on_delete=models.CASCADE, related_name='cars', null=True)
    opcjonalne_wyposazenie = models.ManyToManyField(AditionalEquipment, related_name='cars')
    photo = models.ImageField(upload_to='cars/%Y/%m/%d', default='no_image.png')


    class Meta:
        db_table = 'car'
        ordering = ('model',)

    def publish(self):
        self.save()

    def __str__(self):
        return f'{self.model.name} {self.nazwa} | {self.silnik.name} - {self.rok_produkcji} | ' \
               f'{self.cena_za_godzine}zl - ' + 'Dostępny' if self.dostepnosc else 'Niedostępny' 

                
