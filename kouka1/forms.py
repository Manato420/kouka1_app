from django import forms

class Kouka1Form(forms.Form):
    name  = forms.CharField(label='名前',max_length=30)
    age = forms.IntegerField(label='年齢')
    phone_number = forms.CharField(label='電話番号',max_length=11)
    email = forms.EmailField(label='メール')
    address = forms.CharField(label='住所',max_length=100)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = '名前を入力'
        self.fields['age'].widget.attrs['class'] = 'form-control'
        self.fields['age'].widget.attrs['placeholder'] = '年齢を入力'
        self.fields['phone_number'].widget.attrs['class'] = 'form-control'
        self.fields['phone_number'].widget.attrs['placeholder'] = '電話番号を入力'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスを入力'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['placeholder'] = '住所を入力'