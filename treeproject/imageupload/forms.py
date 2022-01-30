from django import forms

from .models import Tree_Project


class Tree_ProjectForm(forms.ModelForm):
	class Meta:
		model = Tree_Project
		fields = ('name', 'email', 'treeimage')
