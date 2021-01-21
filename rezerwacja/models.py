from django.db import models
from users.models import Account

class Miejsce(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'miejsce'
        verbose_name_plural = 'miejsca'

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class Rezerwacja(models.Model):
    osoba_wypozyczajaca = models.ForeignKey('users.Account', on_delete=models.CASCADE)
    auto_wypozyczane = models.ForeignKey('wypozyczalnia.Car', on_delete=models.CASCADE)
    miejsce_odbioru = models.ForeignKey(Miejsce, on_delete=models.CASCADE, related_name='miejsce_odbioru', null=True)
    data_odbioru = models.DateField()
    godzina_odbioru = models.TimeField()
    miejsce_zwrotu = models.ForeignKey(Miejsce, on_delete=models.CASCADE, related_name='miejsce_zwrotu', null=True)
    data_zwrotu = models.DateField()
    godzina_zwrotu= models.TimeField()

    class Meta:
        db_table = 'rezerwacja'
        ordering = ('data_odbioru',)
        verbose_name_plural = 'rezerwacje'

    def publish(self):
        self.save()

    def __str__(self):
        return f'{self.miejsce_odbioru.name} {self.data_odbioru} {self.godzina_odbioru} {self.miejsce_zwrotu.name} {self.data_zwrotu} {self.godzina_zwrotu}'

