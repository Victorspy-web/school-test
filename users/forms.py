from django import forms


class EmailForm(forms.Form):
    message = forms.CharField(
        required=True,
        label="Your Message",
        widget=forms.Textarea(attrs={
			
		})
    )