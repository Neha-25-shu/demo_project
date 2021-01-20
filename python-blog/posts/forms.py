from django import forms
from tinymce.widgets import TinyMCE
from .models import Post, Comment


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class Contactform(forms.Form):
    countries = [("IN", "INDIA"), ("USA", "AMERICA")]
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "special"}))
    email = forms.EmailField(required=False)
    phone = forms.RegexField(regex="^[6-9][0-9]{9}$", required=False)
    massage = forms.CharField(max_length=500)
    country = forms.ChoiceField(choices=countries)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        phone = cleaned_data.get("phone")
        if email == "" and phone == "":
            raise forms.ValidationError(
                "Atleast email or phone number should be provided", code="invalid"
            )


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "md-textarea form-control",
                "placeholder": "content here ...",
                "rows": "4",
            }
        )
    )

    class Meta:
        model = Post
        fields = (
            "title",
            "overview",
            "content",
            "thumbnail",
            "categories",
            "featured",
            "previous_post",
            "next_post",
        )


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Type your comment",
                "id": "usercomment",
                "rows": "4",
            }
        )
    )

    class Meta:
        model = Comment
        fields = ("content",)
