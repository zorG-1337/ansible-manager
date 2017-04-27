from django import forms
from django.conf import settings

from core import models


class Search(forms.Form):
    name = forms.CharField(required=False)
    hosts = forms.ModelMultipleChoiceField(required=False, queryset=models.Host.objects.all(),
                                           widget=forms.SelectMultiple(attrs={'class': 'need-select2'}))
    host_groups = forms.ModelMultipleChoiceField(label='Groups', required=False, queryset=models.HostGroup.objects.all(),
                                                 widget=forms.SelectMultiple(attrs={'class': 'need-select2'}))


class Edit(forms.ModelForm):
    hosts = forms.ModelMultipleChoiceField(queryset=models.Host.objects.all(), required=False,
                                           widget=forms.SelectMultiple(attrs={'class': 'need-select2'}))
    host_groups = forms.ModelMultipleChoiceField(queryset=models.HostGroup.objects.all(), required=False,
                                                 widget=forms.SelectMultiple(attrs={'class': 'need-select2'}))
    playbook = forms.FilePathField(path=settings.ANSIBLE_PLAYBOOKS_PATH, match='.*\.yml$',
                                   widget=forms.Select(attrs={'class': 'need-select2'}))
    ansible_user = forms.ModelChoiceField(queryset=models.AnsibleUser.objects.all(),
                                          widget=forms.Select(attrs={'class': 'need-select2'}))

    class Meta:
        model = models.TaskTemplate
        exclude = ('vars',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ansible_user'].initial = models.AnsibleUser.objects.first()
        self.fields['playbook'] =  forms.FilePathField(path=settings.ANSIBLE_PLAYBOOKS_PATH, match='.*\.yml$',
                                   widget=forms.Select(attrs={'class': 'need-select2'}))



