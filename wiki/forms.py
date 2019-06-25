from django.forms import ModelForm
from .models import UserFileUpload
# Form used to setup the file upload system.
class UploadFileForm(ModelForm):
    class Meta:
        model = UserFileUpload #UserFileUpload model created 
        fields = ['upload' ]