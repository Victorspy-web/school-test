from django.forms import ModelForm
from .models import Student

class StudentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = Student
        fields = ['picture', 'first_name', 'last_name',
            'other_names', 'age', 'email', 'telephone', 'program']