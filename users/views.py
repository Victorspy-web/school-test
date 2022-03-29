from django.shortcuts import  render, get_object_or_404
from .forms import EmailForm
from django.core.mail import send_mail
from students.models import Student


def send_student_mail(request, pk):
    # retrive post by id
    student = get_object_or_404(Student, id=pk)
    sent = False

    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = f"Message From OpenLaps Administration"
            message = f"{cd['message']}"
            send_mail(subject, message, 'info@openlabs.com', [student.email])
            sent = True
    else:
        form = EmailForm()

    context = {
        'student': student,
        'form': form,
        'sent': sent
    }

    return render(request, 'account/mail.html', context)