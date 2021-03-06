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
        return f'{self.name} | moc - {self.power} spalanie - {self.consumation} l |  typ paliwa - {self.fuel_type} '


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


class Segment(models.Model):
    name = models.CharField(max_length=1, unique = True)

    class Meta:
        db_table = 'segment'

    def publish(self):
        self.save()

    def __str__(self):
        return self.name


class Car(models.Model):
    nazwa = models.CharField(max_length=20)
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='cars', null=True)
    segment = models.ForeignKey(Segment, on_delete=models.CASCADE, related_name='cars', null=True)
    rok_produkcji = models.IntegerField()
    cena_za_godzine = models.IntegerField()
    dostepnosc = models.BooleanField(default=True)
    klimatyzacja = models.BooleanField(default=True)
    ilosc_drzwi = models.IntegerField()
    silnik = models.ForeignKey(Engine, on_delete=models.CASCADE, related_name='cars', null=True)
    opcjonalne_wyposazenie = models.ManyToManyField(AditionalEquipment, related_name='cars')
    zdjecie = models.ImageField(upload_to='cars/%Y/%m/%d', default='no_image.png')
    

    class Meta:
        db_table = 'car'
        ordering = ('model',)

    def publish(self):
        self.save()

    def set_dostepnosc(self, new_dostepnosc):
        self.dostepnosc=new_dostepnosc

    def get_opcjonalne_wyposazenie(self):
        return "\n".join([p.name for p in self.opcjonalne_wyposazenie.all()])

    def getKlimatyzacja(self):
        return 'Jest klimatyzacja' if self.klimatyzacja else 'Brak klimatyzacji'

    def getDostepnosc(self):
        return 'Dostępny' if self.dostepnosc else 'Niedostępny'

    def __str__(self):
        return f'{self.model.name} {self.nazwa} {self.segment.name} {self.rok_produkcji} {self.cena_za_godzine} {self.ilosc_drzwi} {self.silnik}'

RATE_CHOICES = [
	(0,0),
	(1,1),
	(2,2),
	(3,3),
	(4,4),
	(5,5),
]

class Rating(models.Model):
    user = models.ForeignKey('users.Account', on_delete=models.CASCADE)
    car= models.ForeignKey('wypozyczalnia.Car', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
    text = models.TextField(blank = True)

    class Meta:
        verbose_name_plural = 'ocena'

    def publish(self):
        self.save()

    def __str__(self):
        return self.user.username

