from django import forms
from publist.models import Pub

class AddPub(forms.ModelForm):
	name = forms.CharField(required=True)
	address = forms.CharField(required=True)
	area = forms.CharField(required=True)
	county = forms.CharField(required=True)
	thisyear = forms.BooleanField(required=False)
	fromapp = forms.BooleanField(required=False)

	class Meta:
		fields = ('name', 'address', 'area', 'county', 'thisyear', 'fromapp')
