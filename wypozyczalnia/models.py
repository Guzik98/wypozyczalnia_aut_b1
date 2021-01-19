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
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='cars', null=True)
    rok_produkcji = models.IntegerField()
    cena_za_godzine = models.IntegerField()
    dostepnosc = models.BooleanField(default=True)
    klimatyzacja = models.BooleanField(default=True)
    ilosc_drzwi = models.IntegerField()
    ocena = models.FloatField(default=0)
    silnik = models.ForeignKey(Engine, on_delete=models.CASCADE, related_name='cars', null=True)
    opcjonalne_wyposazenie = models.ManyToManyField(AditionalEquipment, related_name='cars')
    photo = models.ImageField(upload_to='cars/%Y/%m/%d', default='no_image.png')
    class Meta:
        db_table = 'car'
        ordering = ('model',)

    def publish(self):
        self.save()

    def set_OpcjonalneWyposarzenie(self,opcjonalne_wyposazenie):
        self.opcjonalne_wyposazenie = opcjonalne_wyposazenie

    def get_opcjonalne_wyposazenie(self):
        return "\n".join([p.name for p in self.opcjonalne_wyposazenie.all()])

    def getKlimatyzacja(self):
        return 'Jest klimatyzacja' if self.klimatyzacja else 'Brak klimatyzacji'

    def getDostepnosc(self):
        return 'Dostępny' if self.dostepnosc else 'Niedostępny'

    def __str__(self):
        return f'{self.model.name} {self.nazwa} {self.rok_produkcji} {self.cena_za_godzine} {self.ilosc_drzwi} {self.ocena} {self.model} {self.silnik} {self.opcjonalne_wyposazenie}'