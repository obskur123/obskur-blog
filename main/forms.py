from django import forms


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.ImageField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput)
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class PostForm(forms.Form):
    title = forms.CharField(max_length=64)
    body = forms.CharField(widget=forms.Textarea)
    files = MultipleFileField()


class CommentForm(forms.Form):
    content = forms.CharField(label="", max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}))
