# -*- coding: utf-8 -*-

from django import forms

from app.models import Customers


# -----------------------------------------------------------------------------
# User
# -----------------------------------------------------------------------------

class CustomerCreationForm(forms.ModelForm):
    """Custom Customer"""

    class Meta():
        model = Customers
        fields = [
            "email",
            "username",
            "password",
            "image",
            "is_active",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(CustomerCreationForm, self).clean()
        email = cleaned_data.get("email")
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        image = cleaned_data.get("image")
        is_active = cleaned_data.get("is_active")
       
        if not email :
            raise forms.ValidationError(
                "Please add email."
            )
        if not username :
            raise forms.ValidationError(
                "Please add username."
            )
        if not image :
            raise forms.ValidationError(
                "Please add image."
            )
        if not password :
            raise forms.ValidationError(
                "Please add password."
            )
        if not is_active :
            raise forms.ValidationError(
                "Please add is_active."
            )

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance


class CustomerChangeForm(forms.ModelForm):
    """Custom form to change customer"""

    class Meta():
        model = Customers

        fields = [
            "email",
            "username",
            "image",
            "password",
            "is_active",
        
        ]

    def clean(self):
        cleaned_data = super(CustomerChangeForm, self).clean()
        email = cleaned_data.get("email")
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        image = cleaned_data.get("image")
        is_active = cleaned_data.get("is_active")
       
        if not email :
            raise forms.ValidationError(
                "Please add email."
            )
        if not username :
            raise forms.ValidationError(
                "Please add username."
            )
        if not image :
            raise forms.ValidationError(
                "Please add image."
            )
        if not password :
            raise forms.ValidationError(
                "Please add password."
            )
        if not is_active :
            raise forms.ValidationError(
                "Please add is_active."
            )

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance