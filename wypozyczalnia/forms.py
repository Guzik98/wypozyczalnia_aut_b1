from django import forms
from .models import Car, Segment,  Rating
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator, ValidationError

class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = (_('nazwa'),
        _('segment'),
        _('rok_produkcji'),
        _('cena_za_godzine'),
        _('dostepnosc'),
        _('klimatyzacja'),
        _('ilosc_drzwi'),
        _('model'),
        _('silnik'),
        _('opcjonalne_wyposazenie'),
        _('zdjecie'),)

        
    

class SegmentForm(forms.ModelForm):
    class Meta: 
        model = Segment
        #name = forms.CharField(validators=[Segment_validacja], label = 'nazwa')
        labels = {
            "name": "Nazwa",
        }
        fields = ('name',)
        

    def Segment_validacja(self):
        for segment in Segment.objects.all():
            if segment.name == name:
                raise forms.ValidationError('Istniejący segment')


def WalidacjaKomentarza(value):
    if len(value)>150 or len(value)<10:
         raise ValidationError('Upewnij się że zawiera od 10 do 150 znaków.')

class RatingForm(forms.ModelForm):
    komentarz = forms.CharField(validators = [WalidacjaKomentarza],widget=forms.Textarea)
    ocena = forms.FloatField(
        validators = [
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )
    class Meta:
        model = Rating
        fields =('ocena', 'komentarz')
    
      

        
        
