from __future__ import unicode_literals
import django_tables2 as tables
from .models import Post
from . import models
from django_tables2.utils import A
from . import views
from django.utils.safestring import mark_safe
from django_tables2.export.export import TableExport


class TrackerTable(tables.Table):
    export_formats = ['csv', 'xls', 'xlsx', 'json']
    id = tables.Column()
    id = tables.LinkColumn('posts:tracker_view',args=[A('pk')], empty_values=())
    editable = tables.LinkColumn('posts:modify',args=[A('pk')] , empty_values=(), verbose_name='')
    #selection = tables.CheckBoxColumn(accessor='pk', attrs = { "th__input":{"onclick": "toggle(this)"}},orderable=False)
    selection = tables.CheckBoxColumn(accessor='pk', attrs = { "th__input":{"onclick": "toggle(this)"}})
    def render_editable(self):
        #return 'Edit'
        return mark_safe('<center><p style="color:blue;">&#9997;</p></center>')


    class Meta:
        model = models.Post
        template_name = 'django_tables2/semantic.html'
        sequence = ('selection','editable','id','...')
        #attrs = {'class': 'table table-bordered', 'tbody': {'id': 'value'}}
        attrs = {'tbody': {'id': 'myTable'}}
