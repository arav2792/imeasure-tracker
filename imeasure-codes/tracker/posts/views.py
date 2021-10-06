from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from . import forms
from .models import Post
from .forms import CreateArticle
from django.http import HttpResponse
from django.contrib.auth.forms import UserChangeForm
from .tables import TrackerTable
from django_tables2 import RequestConfig
from .filters import TrackerFilter
from .filters import PendingFilter
from django_tables2.export.export import TableExport
from .models import Schedules
from .filters import UnattendedFilter

@login_required
def quicklinkview(request):
    return render(request, 'posts/quicklinks.html')

#def tracker_list(request):
#    tracks = Post.objects.all()
#    return render(request,'posts/tracker_list.html',{'tracks':tracks})
@login_required
def tracker_list(request):
    table = TrackerTable(Post.objects.all(), order_by="-id")
    #filter = AFilter(request.GET, queryset=table)
    RequestConfig(request, paginate={'per_page': 100}).configure(table)
    export_format = request.GET.get('_export', None)
    if TableExport.is_valid_format(export_format):
        exporter = TableExport(export_format, table, exclude_columns=('editable','selection'))
        return exporter.response('table.{}'.format(export_format))

    return render(request, 'posts/tracker_list.html', {'table': table})

@login_required
def tracker_view(request, track_id):
    #post = Post.objects.get(pk=post_id)
    track = get_object_or_404(Post, pk=track_id)
    return render(request, 'posts/tracker_view.html', {'track':track})

@login_required
def tracker_edit(request, track_id=None, template_name='posts/tracker_edit.html'):
    if track_id is not None:
        track = get_object_or_404(Post, pk=track_id)
    else:
        track = Post()
    tracker = CreateArticle(request.POST or None, instance=track)
    if request.POST and tracker.is_valid():
        tracker.save()
        redirect_url = reverse('posts:tracker_list')
        return redirect(redirect_url)

    return render(request, template_name, {
        'tracker': tracker
    })

@login_required
def search(request):
    tracker_list = Post.objects.all()
    tracker_filter = TrackerFilter(request.GET, queryset=tracker_list)
    return render(request, 'posts/search.html', {'filter': tracker_filter})

@login_required
def pending(request):
    pending_list = Post.objects.all()
    pending_filter = PendingFilter(request.GET, queryset=pending_list)
    return render(request, 'posts/pending.html', {'filter': pending_filter})

@login_required
def schedule(request):
    schedules = Schedules.objects.all()
    return render(request, 'posts/engschedule.html', {'schedules':schedules})

@login_required
def unattended(request):
    unattended_list = Post.objects.all()
    unattended_filter = UnattendedFilter(request.GET, queryset=unattended_list)
    return render(request, 'posts/unattended.html', {'filter': unattended_filter})




























'''
def tracker_edit(request):
    if request.method == 'POST':
        tracker = forms.CreateArticle(request.POST)
        if tracker.is_valid():
            #save article to db
            tracker.save()
            return redirect('posts:tracker_list')
    else:
        tracker = forms.CreateArticle()
    return render(request, 'posts/tracker_edit.html',{'tracker':tracker})

def tracker_list(request, track_id=None):
    if request.method == 'POST':
        pks = request.POST.getlist("selection")
        table = TrackerTable(Post.objects.filter(pk__in=pks))
    else:
        table = TrackerTable(Post.objects.all(), order_by="-id")
        #filter = AFilter(request.GET, queryset=table)
    RequestConfig(request).configure(table)
    export_format = request.GET.get('_export', None)
    if TableExport.is_valid_format(export_format):
        exporter = TableExport(export_format, table, exclude_columns=('editable','selection'))
        return exporter.response('table.{}'.format(export_format))

    return render(request, 'posts/tracker_list.html', {'table': table})


def tracker_list(request):
    table = TrackerTable(Post.objects.all(), order_by="-id")
    #filter = AFilter(request.GET, queryset=table)
    RequestConfig(request).configure(table)
    export_format = request.GET.get('_export', None)
    if TableExport.is_valid_format(export_format):
        exporter = TableExport(export_format, table, exclude_columns=('editable','selection'))
        return exporter.response('table.{}'.format(export_format))

    return render(request, 'posts/tracker_list.html', {'table': table})
'''
