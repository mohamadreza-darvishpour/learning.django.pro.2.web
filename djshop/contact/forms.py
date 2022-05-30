from django  import forms      
 

class contact_us_form(forms.Form):
    full_name = forms.CharField(label="first-last-family")
    email = forms.EmailField(label="email",widget=forms.EmailInput)
    subject = forms.CharField(label="subj-",
    max_length =50,
    required = True,
    error_messages={
        'required':"enter subject."
    },
    )
    text = forms.CharField(label="the text",widget=forms.TextInput)