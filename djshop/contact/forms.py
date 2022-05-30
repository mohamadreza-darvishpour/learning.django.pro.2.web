from django  import forms      
 

class contact_us_form(forms.Form):
    full_name = forms.CharField(
        label="first-last-family",
        widget=forms.TextInput(
            attrs={
                'class':"col-md-6 form-control",
                'placeholder':"full_name",
            }
        )    
        )
 
    email = forms.EmailField(
        label="email",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control col-md-6',
                'placeholder':"email",
            }
        )
        )
    subject = forms.CharField(label="subj-",
    max_length =50,
    required = True,
    error_messages={
        'required':"enter subject."
    },
    widget=forms.TextInput(
            attrs={
                'class':'form-control col-md-12',
                'placeholder':"text",
                'rows':"3",
                'cols':'5',
                'id':'message',
            }
        )
    )
    text = forms.CharField(label="the text",widget=forms.TextInput(
            attrs={
                'class':'form-control col-md-12',
                'placeholder':"text",
            }
        )
        )