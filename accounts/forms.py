from django import forms
from accounts.models import Staff, Student, School, Batch
from django.contrib.auth.models import Group
from django.forms.widgets import TimeInput, TextInput, DateTimeInput, HiddenInput, NumberInput, Select, DateInput
import datetime

class StaffSignupForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
    }
    password1 = forms.CharField(label="Password",
        widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation",
        widget=forms.PasswordInput)

    class Meta:
        model = Staff
        fields = ("username","email","first_name","last_name","phone_number")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2


    def save(self, school, commit=True):
        staff = super(StaffSignupForm, self).save(commit=False)
        staff.set_password(self.cleaned_data["password1"])
        is_super = self.data.get("is_super_staff")
        if not is_super:
            staff.is_super_staff = False
        else:
            staff.is_super_staff = is_super=='on'
        staff.is_active = True
        staff.staff_school = school

        if commit:
            staff.save()
            group = Group.objects.get(name='Staff')
            staff.groups.add(group)

        return staff


class StaffUpdateForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ("email", "first_name", "last_name", "phone_number", "is_super_staff")


class SchoolSignupForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
    }
    password1 = forms.CharField(label="Password",
        widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation",
        widget=forms.PasswordInput)

    class Meta:
        model = School
        fields = ("username","email","full_name","phone_number", "address","city","state","zip_code","country")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self,commit=True):
        school = super(SchoolSignupForm, self).save(commit=False)
        school.set_password(self.cleaned_data["password1"])
        school.is_active = True
        if commit:
            school.save()
            group = Group.objects.get(name='School')
            school.groups.add(group)

        return school


class StudentCreationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class BatchForm(forms.ModelForm):
    year = forms.ChoiceField(widget=forms.Select(), required=True)
    class Meta:
        widgets = {
            'application_acceptance_start_at': DateInput(attrs={'class':'datepicker'}),
            'application_acceptance_end_at': DateInput(attrs={'class':'datepicker'}),
        }
        model = Batch
        exclude = ("batch_school","is_current")

    def __init__(self, *args, **kwargs):
        self.base_fields['year'].choices = [
            (str(i), str(i)) for i in range(datetime.datetime.now().year, (datetime.datetime.now().year + 10))
            ]
        super(BatchForm, self).__init__(*args, **kwargs)

    def save(self, school, commit=True):
        batch = super(BatchForm, self).save(commit=False)
        batch.is_current = True
        batch.batch_school = school
        if commit:
            batch.save()
        return batch

class UploadApplicationForm(forms.Form):
    file = forms.FileField()
