from collections import OrderedDict

from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, DetailView
from formtools.wizard.views import NamedUrlSessionWizardView
from .models import WizardResponse



class Form1(forms.ModelForm):
    class Meta:
        model = WizardResponse
        fields =('response_1_1', 'response_1_2',)


class Form2(forms.ModelForm):
    class Meta:
        model = WizardResponse
        fields =('response_2_1', 'response_2_2',)


class Form3(forms.ModelForm):
    class Meta:
        model = WizardResponse
        fields =('response_3_1', 'response_3_2',)


FORMS = [
    ('1', Form1),
    ('2', Form2),
    ('3', Form3),
]

TEMPLATES = {
    '1': "step1.html",
    '2': "step2.html",
    '3': "step3.html",
    'done': "done.html",
}


class WizardView(NamedUrlSessionWizardView):

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        instance = WizardResponse.objects.create(**self.get_all_cleaned_data())
        return redirect(reverse('done', args=(instance.id,)))

    def previous_steps(self, current_step):
        for step in OrderedDict(self.form_list).keys():
            if step == current_step:
                raise StopIteration()
            yield step

    def get(self, *args, **kwargs):
        for step in self.previous_steps(self.kwargs['step']):
            form = self.get_form(
                step,
                data=self.storage.data['step_data'].get(step, {}),
                files=self.storage.data['step_files'].get(step, {})
            )
            if not form.is_valid():
                return redirect(self.get_step_url(step))
        return super().get(*args, **kwargs)

    def get_context_data(self, form, **kwargs):
        context = super().get_context_data(form, **kwargs)
        context['data_so_far'] = self.get_all_cleaned_data()
        return context


class DoneView(DetailView):
    template_name = 'done.html'
    model = WizardResponse


class IndexView(TemplateView):
    template_name = 'index.html'
