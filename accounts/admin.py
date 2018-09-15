from django.contrib import admin
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.utils.translation import ugettext_lazy as _

from django.contrib.auth import get_user_model

from .models import *

User = get_user_model()

class SchoolCreationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = School
        exclude = ('created_at', 'updated_at', 'is_active', 'is_superuser', 'is_staff', 'is_admin')

    def clean_password_confirm(self):

        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords don't match")
        return


    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(SchoolCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            group = Group.objects.get(name='School')
            user.groups.add(group)
            user.save()
        return user


class SchoolChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField(label=_("Password"),
                                         help_text=_("Raw passwords are not stored, so there is no way to see "
                                                     "this user's password, but you can change the password "
                                                     "using <a href=\"../password/\">this form</a>."))

    class Meta:
        model = School
        exclude = ('is_superuser', 'is_staff', 'is_admin')

    def clean_password(self):
        return self.initial["password"]


class StaffCreationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Staff
        exclude = ('created_at', 'updated_at', 'is_superuser', 'is_staff', 'is_admin')

    def clean_password_confirm(self):

        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords don't match")
        return


    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(StaffCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            group = Group.objects.get(name='Staff')
            user.groups.add(group)
        return user


class StaffChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField(label=_("Password"),
                                         help_text=_("Raw passwords are not stored, so there is no way to see "
                                                     "this user's password, but you can change the password "
                                                     "using <a href=\"../password/\">this form</a>."))

    class Meta:
        model = Staff
        exclude = ('is_superuser', 'is_staff', 'is_admin')

    def clean_password(self):
        return self.initial["password"]

# class StaffInlineAdmin(admin.StackedInline):
#     model = Staff
#     # add_form = StaffCreationForm
#     # form = StaffChangeForm
#     form = StaffCreationForm
#     fk_name = "staff_school"
#     extra = 1
#
#     fieldsets = (
#         (None, {'fields': ('username', 'password', 'password_confirm')}),
#         (_('Staff info'), {'fields': ('email', 'first_name', 'last_name', 'phone_number')}),
#         (_('Permissions'), {'fields': ('is_super_staff','is_active')}),
#     )

class SchoolAuthAdmin(BaseUserAdmin):

    add_form = SchoolCreationForm
    form = SchoolChangeForm

    list_display = ['full_name', 'email', 'address', 'phone_number', 'city', 'country', 'is_active']
    search_fields = ('email', 'username')

    # inlines = [StaffInlineAdmin]


    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('School info'), {'fields': ('email', 'full_name', 'address', 'phone_number',  'city', 'state', 'country', 'zip_code')}),
        (_('Permissions'), {'fields': ('is_active', 'groups')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password', 'password_confirm')}
         ),
    )


class StaffAuthAdmin(BaseUserAdmin):

    add_form = StaffCreationForm
    form = SchoolChangeForm

    list_display = ['first_name', 'last_name', 'email', 'phone_number', 'staff_school', 'is_active', 'is_super_staff']
    search_fields = ('email', 'username')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Staff info'), {'fields': ('email', 'first_name', 'last_name', 'phone_number')}),
        (_('School info'), {'fields': ('staff_school',)}),
        (_('Permissions'), {'fields': ('is_active','is_super_staff')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'staff_school', 'password', 'password_confirm')}
         ),
    )

class StudentAdminModel(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth', 'gender']

admin.site.register(School, SchoolAuthAdmin)
admin.site.register(Staff, StaffAuthAdmin)
admin.site.register(Student, StudentAdminModel)

