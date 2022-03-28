from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages



from django.urls import reverse_lazy

from .models import Student
from .forms import StudentForm

# Create your views here.


class StudentMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = Student
    success_url = reverse_lazy('students:list_students')
    context_object_name = 'students'


class StudentEditMixin(StudentMixin):
    template_name = 'students/student_form.html'
    form_class = StudentForm


class StudentListView(StudentMixin, ListView):
    template_name = 'students/student_list.html'


class StudentCreateView(StudentEditMixin, CreateView):
    success_message = 'New student created successfully'


class StudentUpdateView(StudentEditMixin, UpdateView):
    success_message = 'Student updated successfully'


class StudentDeleteView(StudentMixin, DeleteView):
    template_name = 'students/student_delete.html'
    context_object_name = 'student'
    success_message = 'Student deleted successfully'
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(StudentDeleteView, self).delete(request, *args, **kwargs)


class StudentDetailView(StudentEditMixin, DetailView):
    template_name = 'students/student_detail.html'
    context_object_name = 'student'
