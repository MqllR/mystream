from pprint import pprint
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StreamForm

from .extras.utils import handle_uploaded_file

# Create your views here.

def upload_file(request):
    if request.method == 'POST':
        form = StreamForm(request.POST, request.FILES)

        if form.is_valid():
            if handle_uploaded_file(request.FILES['stream_file']):
                thr = Encode('media/tmp/.' + request.FILES['stream_file'].name)
                thr.start()
                return HttpResponseRedirect('/library/encoding_process/')
            else: 
                return HttpResponseRedirect('/library/error/')

    else:
        form = StreamForm()

    return render(request, 'upload.html', {'form': form})

