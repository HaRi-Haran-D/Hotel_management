from django import forms

class AvailabilityForm(forms.Form):
    ROOM_CATEGORIES = (
        ('YAC','AC'),
        ('NAC','NON-AC'),
        ('DEL','DELUXE'),
        ('KIN','KING'),
        ('QUE','QUEEN'),
    )
    room_category = forms.ChoiceField(choices=ROOM_CATEGORIES, required=True)

    check_in = forms.DateField(
        required=True, input_formats=['%Y-%m-%d'], 
        widget=forms.DateInput(attrs={'type':'date'})
        )
    
    check_out = forms.DateField(
        required=True, input_formats=['%Y-%m-%d'], 
        widget=forms.DateInput(attrs={'type':'date'})
        )
