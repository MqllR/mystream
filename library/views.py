from pprint import pprint

import operator

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.views.generic import ListView, DetailView


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

            return HttpResponseRedirect('/admin/library/stream/encoding_process/')

    else:
        form = StreamForm()

    return render(request, 'upload.html', {'form': form})


class StreamListView(ListView):

    template_name = 'stream_list.html'
    context_object_name = "streams"

    def get_queryset(self):
        cat = self.kwargs.get('category', 'None')

        if not cat == 'None':
            if cat == 'movie':
                return Stream.objects.filter(encoded=1, category__name='movie')
            elif cat == 'serie':
                return Stream.objects.filter(encoded=1, category__name='serie')
        else:
            return Stream.objects.filter(encoded=1)

class StreamSearchListView(StreamListView):

    def get_queryset(self):
        result = super(StreamSearchListView, self).get_queryset()

        query = self.request.GET.get('q')

        if query:
            query_list = query.split()

            result = result.filter(
                reduce(operator.and_,
                       (Q(name__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(description__icontains=q) for q in query_list))
            )

            pprint(result)
            return result

class StreamDetailView(DetailView):

    template_name = 'stream_view.html'
    context_objects_name = 'stream'

    def get_object(self):
        return Stream.objects.get(id=self.kwargs['stream_id'])

class StreamViewDetailView(DetailView):

    template_name = 'stream_viewer.html'
    context_objects_name = 'stream'

    def get_context_data(self, **kwargs):
        context = super(StreamViewDetailView, self).get_context_data(**kwargs)
        context['base_path'] = settings.MEDIA_URL

        return context

    def get_object(self):
        return Stream.objects.get(id=self.kwargs['stream_id'])
