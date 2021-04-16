from django import forms

class blank(forms.Form):
    name=forms.CharField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    email = forms.EmailField(max_length = 200)
    roll=forms.IntegerField()




class sd(forms.Form):
    m1=forms.IntegerField()
    m3=forms.IntegerField()
    m5=forms.IntegerField()
    m10=forms.IntegerField()
    m15=forms.IntegerField()
    m30=forms.IntegerField()
    h1=forms.IntegerField()
    h3=forms.IntegerField()
    h8=forms.IntegerField()
    h15=forms.IntegerField()
    h24=forms.IntegerField()
    d2=forms.IntegerField()
    d7=forms.IntegerField()
