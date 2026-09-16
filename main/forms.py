from django.forms import ModelForm, Select, Textarea, TextInput, URLInput
from main.models import Experience


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "category",
            "description",
            "thumbnail",
        ]
        labels = {
            "title": "Judul Pengalaman",
            "category": "Kategori",
            "description": "Deskripsi",
            "thumbnail": "URL Gambar/Thumbnail",
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
        }