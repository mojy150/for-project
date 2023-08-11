from django import forms


class UserRegistrationForm(forms.Form):
    username = forms.CharField(label="نام کاربری" , widget=forms.TextInput(attrs={'placeholder': 'نام کاربری خود را وارد کنید...'}),required=True)
    email = forms.EmailField(label="ایمیل" , widget=forms.TextInput(attrs={'placeholder': 'ایمیل خود را وارد کنید...'}),required=True)
    password = forms.CharField(label="کلمه عبور" , widget=forms.TextInput(attrs={'placeholder': 'کلمه عبور خود را وارد کنید...'}),required=True)
    
class UserLoginForm(forms.Form):
    username = forms.CharField(label="نام کاربری" , widget=forms.TextInput(attrs={'placeholder': 'نام کاربری خود را وارد کنید...'}),required=True)
    password = forms.CharField(label="کلمه عبور" , widget=forms.TextInput(attrs={'placeholder': 'کلمه عبور خود را وارد کنید...'}),required=True)