from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, Select, Textarea, TextInput, URLInput, DateTimeInput
from main.models import Experience, Project

SECRET_PASSCODE = "220107"

class ExperienceForm(ModelForm):
    secret_passcode = forms.CharField(
        label="PIN",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Masukkan PIN untuk menyimpan"}
        ),
        required=True,
    )

    class Meta:
        model = Experience
        fields = [
            "title",
            "category",
            "description",
            "thumbnail",
            "ended_at",
        ]
        labels = {
            "title": "Judul Pengalaman",
            "category": "Kategori",
            "description": "Deskripsi",
            "thumbnail": "URL Gambar/Thumbnail",
            "ended_at": "Tanggal Selesai",
        }
        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Contoh: PBP Teaching Assistant",
                    "maxlength": 255,
                }
            ),
            "category": Select(),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan pengalaman dan peranmu...",
                    "rows": 3,
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
            "ended_at": DateTimeInput(
                attrs={
                    "type": "datetime-local",
                }
            ),
        }

    def clean_secret_passcode(self):
        passcode = self.cleaned_data.get("secret_passcode")
        if passcode != SECRET_PASSCODE:
            raise ValidationError("PIN salah! Perubahan dibatalkan.")
        return passcode

class ProjectForm(ModelForm):
    secret_passcode = forms.CharField(
        label="PIN",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Masukkan PIN untuk menyimpan"}
        ),
        required=True,
    )

    class Meta:
        model = Project
        fields = [
            "title",
            "category",
            "description",
            "thumbnail",
        ]
        labels = {
            "title": "Judul Proyek",
            "category": "Kategori",
            "description": "Deskripsi",
            "thumbnail": "URL Gambar/Thumbnail",
        }
        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Contoh: Makanan bergizi gratis",
                    "maxlength": 255,
                }
            ),
            "category": Select(),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan pengalaman dan peranmu...",
                    "rows": 3,
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }

    def clean_secret_passcode(self):
        passcode = self.cleaned_data.get("secret_passcode")
        if passcode != SECRET_PASSCODE:
            raise ValidationError("PIN salah! Perubahan dibatalkan.")
        return passcode