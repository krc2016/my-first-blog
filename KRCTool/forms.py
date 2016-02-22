from django import forms
from .models import KRCrequest, KRCdata, valider

class 	KRCform(forms.ModelForm):
	"""docstring for KRCform"forms.ModeFormf __init__(self, arg):
		super(KRCform,forms.ModeForm.__init__()
		self.arg = arg"""

	class Meta:
		model = KRCrequest
		fields = ('termSource','termTarget')

class 	validerForm(forms.ModelForm):
	"""docstring for KRCform"forms.ModeFormf __init__(self, arg):
		super(KRCform,forms.ModeForm.__init__()
		self.arg = arg"""

	class Meta:
		model = valider
		fields = ('oui','non')