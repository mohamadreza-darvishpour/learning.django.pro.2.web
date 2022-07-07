from django  import forms
from .models import contact_us
class Meta:
        model = None
        fields = ("",)
  
 

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





from .models import contact_us
class contact_model_form(forms.ModelForm):
    class Meta:
        model = contact_us
        fields = ['email','title','full_name','message']   #just show members of field
        #fields = '__all__'     #show all
        #exclude = ['is_read_by_admin']   #show all despite exclude member

class new_glance(forms.Form):
    glance_title = forms.CharField(max_length=200,label="gl_ti")
    glance_email = forms.EmailField(label="gl_em" )
    glance_name = forms.CharField(max_length=200,label="gl_te")
    glance_text  = forms.CharField(label="the text",widget=forms.TextInput(
            attrs={
                'class':'form-control col-md-12',
                'placeholder':"text",
                 
            }
        )
        )
      


class direct_model_form(forms.ModelForm):
    class Meta:
        model = contact_us
        fields = ["title","email","full_name","message"]
        labels={
            'title':"the title<>"
        }
        widgets={
            'title':forms.TextInput(attrs={
                "class":"form-control",
              }),
            'email':forms.TextInput(attrs={
                "class":"form-control",
                "border":"4px solid yellow"
              }),
            'full_name':forms.TextInput(attrs={
                "class":"form-control",
                 
             }),
            'message':forms.Textarea(attrs={
                'border':'2px solid yellow',
                "class":"col-md-9 form-control",
                'rows':6,
                'id':'message',
                 
             }),
        
        }
        errors={
            'title':{
                'required':"insert title man",
            },
        
            'full_name':{
                'required':"insert fullname man",
            },
        
                    'message':{
                'required':"insert message man",
            },
        
                    'email':{
                'required':"insert email man",
            },
        }

    '''
    not direct model to form
    glance_title = forms.CharField(max_length=200,label="gl_ti")
    glance_email = forms.EmailField(label="gl_em" )
    glance_name = forms.CharField(max_length=200,label="gl_te")
    glance_text  = forms.CharField(label="the text",widget=forms.TextInput(
            attrs={
                'class':'form-control col-md-12',
                'placeholder':"text",
                 
            }
        )
        )
        '''
      