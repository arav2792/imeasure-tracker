from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from . import forms
from .models import Update
from .forms import UpdateArticle
from django.http import HttpResponse
from django.contrib.auth.forms import UserChangeForm
from .tables import UpdateTable
from django_tables2 import RequestConfig
from django_tables2.export.export import TableExport


'''
def process_updates(request):
    if request.method == 'POST':
        updates = forms.UpdateArticle(request.POST)
        if updates.is_valid():
            #save article to db
            updates.save()
            return redirect('updates:updates_list')
    else:
        updates = forms.UpdateArticle()
    return render(request, 'updates/process_updates.html',{'updates':updates})
'''
@login_required
def updates_list(request):
    table = UpdateTable(Update.objects.all(), order_by="-id")
    #filter = AFilter(request.GET, queryset=table)
    RequestConfig(request).configure(table)
    export_format = request.GET.get('_export', None)
    if TableExport.is_valid_format(export_format):
        exporter = TableExport(export_format, table, exclude_columns=('editable','selection'))
        return exporter.response('table.{}'.format(export_format))

    return render(request,'updates/updates_list.html',{'table':table})

@login_required
def update_view(request, up_id):
    #post = Post.objects.get(pk=post_id)
    update = get_object_or_404(Update, pk=up_id)
    return render(request, 'updates/update_view.html', {'update':update})

@login_required
def process_updates(request, up_id=None, template_name='updates/process_updates.html'):
    if up_id is not None:
        update = get_object_or_404(Update, pk=up_id)
    else:
        update = Update()
    updates = UpdateArticle(request.POST or None, instance=update)
    if request.POST and updates.is_valid():
        updates.save()
        redirect_url = reverse('updates:updates_list')
        return redirect(redirect_url)

    return render(request, template_name, {
        'updates': updates
    })
