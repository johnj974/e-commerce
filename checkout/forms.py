from django import forms            # django library
from .models import Order           # order object from our models.py file


class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2019, 2036)]

    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)  # month_choices were created above
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)     # year_choices were created above

    stripe_id = forms.CharField(widget=forms.HiddenInput)                    # stripe requires this id that will be hidden from the user


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = (
            'full_name', 'phone_number', 'country', 'postcode',           # fields data comes from order object
            'town_or_city', 'street_address1', 'street_address2',
            'county'
        )