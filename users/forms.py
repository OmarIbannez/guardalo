from users.models import User
from django import forms


class UserRegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        if len(self.cleaned_data['password']) < 8:
            raise forms.ValidationError("Password must be at least 8 characters")

        if self.cleaned_data['confirm_password'] != self.cleaned_data['password']:
            raise forms.ValidationError("Passwords don't match")

        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise forms.ValidationError("A user with this Username already exists")

        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("A user with this Email already exists")
