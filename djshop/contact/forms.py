from django  import forms      
 

class contact_us_form(forms.Form):
    full_name = forms.CharField(label="first-last-family")
    email = forms.EmailField()
    subject = forms.CharField()
    text = forms.CharField()