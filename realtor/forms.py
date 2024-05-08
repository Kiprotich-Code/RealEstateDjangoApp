from django import forms
from .models import Properties
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Row, Column

# Create Forms Here 
class PropertiesForm(forms.ModelForm):
    class Meta:
        model = Properties
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PropertiesForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='col-md-3'),
                Column('address', css_class='col-md-3'),
                Column('price', css_class='col-md-3'),
                Column('amentities', css_class='col-md-3'),
            ),
            Row(
                Column('size', css_class='col-md-3'),
                Column('bedrooms', css_class='col-md-3'),
                Column('bathrooms', css_class='col-md-3'),
                Column('status', css_class='col-md-3'),
                Column('images', css_class='col-md-3'),
            ),
            Row(
                Column('description', css_class='col-md-6'),
                Column('features', css_class='col-md-6'),
            ),
            Submit('submit', u'Create Property', css_class='btn btn-light btn-lg'),
        )