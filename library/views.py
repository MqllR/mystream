from pprint import pprint

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


from .models import Stream, StreamTmp, Category
from .forms import StreamForm
from .tasks import encode_stream
from .extras.savefile import SaveStream

# Create your views here.

@login_required(login_url='/admin/login/')
@csrf_exempt
def upload_file(request):

    if request.method == 'POST':
        form = StreamForm(request.POST)

        if form.is_valid() and request.FILES:
            stream_file = request.FILES['stream_file']
            fs = SaveStream()
            tmpfilename = fs.save(stream_file.name, stream_file)

            # Save streaming file info
            stream_name = form.cleaned_data['stream_name']
            stream_description = form.cleaned_data['stream_description']
            stream_category = form.cleaned_data['stream_category']

            cat = Category.objects.get(name=stream_category)

            stream = Stream(
                name=stream_name,
                description=stream_description,
                category=cat,
            )

            stream.save()

            # Save streaming tmp file info
            StreamTmp(
                tmppath=tmpfilename,
                stream=stream,
            ).save() 

            # Run encoding process in an async task
            encode_stream.delay(tmpfilename) 
            #if handle_uploaded_file(request.FILES['stream_file']):
            #    thr = Encode('media/tmp/.' + request.FILES['stream_file'].name)
            #    thr.start()
            #    return HttpResponseRedirect('/library/encoding_process/')
            #else: 
            return HttpResponseRedirect('/admin/library/stream/encoding_process/')

    else:
        form = StreamForm()

    return render(request, 'upload.html', {'form': form})

