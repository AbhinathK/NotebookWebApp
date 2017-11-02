from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Note
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .forms import NoteSearchForm
from search_views.search import SearchListView
from search_views.filters import BaseFilter

class index(generic.ListView):
    template_name = 'notebooks/index.html'
    context_object_name = 'all_notes'
    paginate_by = 13

    def get_queryset(self):
        return Note.objects.all()


def detail(request, note_id):
    note = get_object_or_404(Note, pk = note_id)
    return render(request, 'notebooks/detail.html', {'note': note})


class NoteCreate(CreateView):
    model = Note
    fields=['note_title','note_description']
    pk_url_kwarg = 'note_id'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self, **kwargs):
        if  kwargs != None:
            return reverse_lazy('notebooks:index')
        else:
            return reverse_lazy('notebooks:home')

class NoteEdit(UpdateView):
    model = Note
    fields=['note_title','note_description']
    pk_url_kwarg = 'note_id'

class NoteDelete(DeleteView):
    model = Note
    success_url = reverse_lazy('notebooks:index')
    pk_url_kwarg = 'note_id'

class NotesFilter(BaseFilter):
    search_fields = {
        'search_title' : ['note_title'],
        'search_author' : ['id', 'author__username'],
        'search_description' : ['note_description'],
        }

class NoteSearchList(SearchListView):
    model = Note
    paginate_by = 30
    context_object_name = 'all_notes'
    template_name = "notebooks/notes_list.html"
    form_class = NoteSearchForm
    filter_class = NotesFilter
