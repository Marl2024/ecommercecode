from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}), 
        required=True
    )
    shipping_email = forms.EmailField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}), 
        required=False
    )
    shipping_address = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}), 
        required=True
    )
    shipping_city = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}), 
        required=True
    )
    shipping_state = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}), 
        required=False
    )
    shipping_zipcode = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip Code'}), 
        required=False
    )
    shipping_country = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}), 
        required=True
    )

    class Meta:
        model = ShippingAddress
        fields = [
            'shipping_full_name', 
            'shipping_email', 
            'shipping_address', 
            'shipping_city', 
            'shipping_state', 
            'shipping_zipcode', 
            'shipping_country'
        ]
        # Optionally, you can exclude fields if necessary
        # exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(ShippingForm, self).__init__(*args, **kwargs)




class BillingForm(forms.ModelForm):
    billing_full_name = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}), 
        required=True
    )
    billing_email = forms.EmailField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}), 
        required=False
    )
    billing_address = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}), 
        required=True

        )

    class Meta:
        model = ShippingAddress
        fields = ['billing_full_name', 'billing_email', 'billing_address']
        # Optionally, you can exclude fields if necessary
        # exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(BillingForm, self).__init__(*args, **kwargs)