from pprint import pprint

import operator

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.shortcuts import Http404
from django.db.models.functions import Lower
from celery import chord


from .models import Stream, StreamTmp, Category
from .forms import StreamForm
from .tasks import encode_stream, post_encoding
from .extras.savefile import SaveStream

# MY OWN VIEW HERE

@login_required(login_url='/admin/login/')
@csrf_exempt
def upload_file(request):
    """
    View form to override the admin admin/add/stream/
    """

    if request.method == 'POST':
        form = StreamForm(request.POST)

        if form.is_valid() and request.FILES:
            stream_file = request.FILES['stream_file']
            fs = SaveStream()
            tmpfilename = fs.save(stream_file.name, stream_file)

            # Save streaming file info
            stream_name = form.cleaned_data['stream_name']
            stream_description = form.cleaned_data['stream_description']
            stream_quality = form.cleaned_data['stream_quality']
            stream_category = form.cleaned_data['stream_category']

            cat = Category.objects.get(name=stream_category)

            stream = Stream(
                name=stream_name,
                description=stream_description,
            )

            stream.category = cat
            stream.save()

            # stream_quality is a list of QuerySet
            # We make the many-to-many relation
            stream.quality = stream_quality

            # Save streaming tmp file info
            StreamTmp(
                tmppath=tmpfilename,
                stream=stream,
            ).save() 

            # Run encoding process in celery tasks with chord primitive
            chord(encode_stream.si(tmpfilename, qual.name) 
                        for qual in stream_quality)(post_encoding.si(tmpfilename))


            return HttpResponseRedirect('/admin/library/stream/encoding_process/')

    else:
        form = StreamForm()

    return render(request, 'upload.html', {'form': form})


class StreamListView(ListView):
    """
    List all streams or by category
    """

    template_name = 'stream_list.html'
    context_object_name = "streams"

    def get_context_data(self, *args, **kwargs):
        context = super(StreamListView, self).get_context_data(*args, **kwargs)
        cat = self.kwargs.get('category', 'None')

        # If cat is equal None, we list all object
        if cat != 'None':
            try:
                category = Category.objects.get(name = cat)
            except Category.DoesNotExist:
                raise Http404

        return context
        

    def get_queryset(self):
        cat = self.kwargs.get('category', 'None')

        if cat == 'None':
            return Stream.objects.filter(encoded=1).order_by(Lower('name'))
        else:
            return Stream.objects.filter(encoded=1, category__name=cat).order_by(Lower('name'))


class StreamSearchListView(ListView):
    """
    List result of the search request
    """

    template_name = 'stream_list.html'
    context_object_name = "streams"

    def get_queryset(self):
        result = Stream.objects.filter(encoded=1)

        query = self.request.GET.get('q')

        if query:
            query_list = query.split()

            result = result.filter(
                reduce(operator.and_,
                       (Q(name__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(description__icontains=q) for q in query_list))
            ).order_by(Lower('name'))

            return result


class StreamDetailView(DetailView):
    """
    Print information of specifique stream
    """

    template_name = 'stream_view.html'
    context_objects_name = 'stream'

    def get_object(self):
        try:
            return Stream.objects.get(id=self.kwargs['stream_id'])
        except Stream.DoesNotExist:
            raise Http404


class StreamViewDetailView(DetailView):
    """
    Print page with video
    """

    template_name = 'stream_viewer.html'
    context_objects_name = 'stream'

    def get_context_data(self, **kwargs):
        context = super(StreamViewDetailView, self).get_context_data(**kwargs)
        context['base_path'] = settings.MEDIA_URL

        return context

    def get_object(self):
        try:
            return Stream.objects.get(id=self.kwargs['stream_id'])
        except Stream.DoesNotExist:
            raise Http404
