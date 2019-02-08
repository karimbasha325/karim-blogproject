from django import forms
class Emailsendview(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    to=forms.EmailField()
    comment=forms.CharField(required=False,widget=forms.Textarea)

from post.models import Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','email','body')
