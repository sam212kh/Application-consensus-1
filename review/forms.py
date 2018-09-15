from django import forms
from accounts.models import Staff, Student, School, Batch
from django.contrib.auth.models import Group
from django.forms.widgets import TimeInput, TextInput, DateTimeInput, HiddenInput, NumberInput, Select, DateInput
import datetime



class ApplicationForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    phone_number = forms.CharField(required=False)
    date_of_birth = forms.DateField(required=True, widget=DateInput(attrs={'class':'datepicker'}))
    gender =  forms.ChoiceField(required=True, widget=forms.RadioSelect(
    attrs={'class': 'Radio'}), choices=(('male','Male'),('female','Female'),))
    school = forms.ChoiceField(widget=forms.Select(), required=True)
    application_text = forms.CharField(required=True,widget=forms.Textarea(attrs={'width':"100%", 'rows': "5"}))
    educational_info = forms.CharField(required=True,widget=forms.Textarea(attrs={'width':"100%", 'rows': "5"}))

    def __init__(self, *args, **kwargs):
        schools = School.objects.filter(school_batches__is_current=True)
        self.base_fields['school'].choices = [
            (str(i.id), str(i.full_name)) for i in schools
        ]
        super(ApplicationForm, self).__init__(*args, **kwargs)


class RateForm(forms.Form):

    rating = forms.ChoiceField(widget=forms.Select(), required=True)
    comment = forms.CharField(required=True,widget=forms.Textarea(attrs={'width':"100%", 'rows': "5", 'cols': "100"}))

    def __init__(self, *args, **kwargs):
        schools = School.objects.filter(school_batches__is_current=True)
        self.base_fields['rating'].choices = [
            (str(i), str(i)) for i in range(1,6)
        ]
        super(RateForm, self).__init__(*args, **kwargs)


class MultipleForm(forms.Form):
    action = forms.CharField(max_length=60, widget=forms.HiddenInput())


class ApplicationSearchForm(MultipleForm):
    search = forms.CharField(label='Search application by id', max_length=200, widget=forms.TextInput)


class ApplicationStatusForm(MultipleForm):
    id = forms.CharField(max_length=60, widget=forms.HiddenInput())
    status = forms.CharField(max_length=60, widget=forms.HiddenInput())
