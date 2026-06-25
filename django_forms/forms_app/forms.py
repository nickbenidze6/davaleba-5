from django import forms
from .models import Student, Book

class StudentForm(forms.Form):
    firstname = forms.CharField(max_length=50, label="firstname",
    widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "Enter your first name"}))

    lastname =  forms.CharField(max_length=50, label="lastname",
    widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "Enter your last name"}))
    
    age =  forms.IntegerField(label="age",
    widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "Enter your age"}))

    course =  forms.CharField(max_length=50, label="course",
    widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "Enter your course"}))

    
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 18:
            raise forms.ValidationError("you are under age 18")
        return age



class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "writed_at",]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'title' 
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'author'
            }),
            'writed_at': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'writed_at'
            }),
        }