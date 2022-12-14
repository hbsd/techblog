from django.forms import ModelForm, widgets
from django import forms
from .models import Post


# Create a new post
class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'image', 'description', 'source', 'tags']
		widgets = {
			'tags': forms.CheckboxSelectMultiple(),
		}

	def __init__(self, *args, **kwargs):
		super(PostForm, self).__init__(*args, **kwargs)

		for name, field in self.fields.items():
			field.widget.attrs.update({'class': 'input'})
