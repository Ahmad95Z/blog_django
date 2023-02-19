from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =('message', )

        widget = {
            'message': forms.TextInput(attrs={'class':'form-control'}),
           }
        

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'image', 'body', 'category',)

        widget = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
           }
    
class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'category',)

        widget = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
        }