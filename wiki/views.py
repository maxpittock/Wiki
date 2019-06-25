from django.views import generic
from .models import Page, UserFileUpload
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
import logging
from django.db.models import F
from django.http import HttpResponse

logger = logging.getLogger(__name__)

#views for the index page.
class IndexView(generic.ListView):
    template_name = 'wiki/index.html'
    context_object_name = 'pages'
    def get_queryset(self):
        return Page.objects.all().order_by('title')
    
#views for the details page
class DetailView(generic.DetailView):
    model = Page
    template_name = 'wiki/detail.html'

#views for the page counter that is on the individual pages
def view_page(request, pk):
    try:
        page = Page.objects.get(pk=pk)
        #page.counter += 1
        page.counter = F('counter') + 1
        page.save(update_fields=['counter'])
        page.refresh_from_db()
        return render(request, 'wiki/detail.html', {'page': page})
    except Page.DoesNotExist:
        return render(request, 'wiki/create_page.html', {'page_name': pk})

#Checks for login
@login_required(login_url='wiki:login')
#Views for edit page
def edit_page(request, pk):
    try:
        page= Page.objects.get(pk=pk)
        content = page.content
    except Page.DoesNotExist:
        content=''
    return render(request, 'wiki/edit_page.html',{ 'page_name':pk, 'content':content},)


@login_required(login_url='wiki:login')
#views for save page
def save_page(request, pk):
    content = request.POST["content"]
    try:
        page = Page.objects.get(pk=pk)
        page.content = content
    except Page.DoesNotExist:
        page = Page(title=pk, content=content)
    if 'Save' in request.POST:
        page.save()
    return redirect(page)

@login_required(login_url='wiki:login')
#view for uploading files
def upload_file(request):
    context = {}
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = UploadFileForm()
    context['form'] = form
    context['files'] = UserFileUpload.objects.all().order_by('upload')
    return render(request, 'wiki/upload.html', context)

#error tests
def error_test(request):
    return HttpResponse(status=404)