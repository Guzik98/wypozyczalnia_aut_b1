from django import forms
from .models import Car, Segment, Rating, RATE_CHOICES
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

class RateForm(forms.ModelForm):
    text = forms.CharField(validators = [WalidacjaKomentarza],widget=forms.Textarea(attrs={'class': 'materialize-textarea'}), label="komentarz")
    rate = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(), required=True, label="ocena")
    class Meta:
        model = Rating
        fields =('text', 'rate')
    
      

        
        
