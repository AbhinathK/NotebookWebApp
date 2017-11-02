from django.conf.urls import url
from . import views
from .models import Note
from django.contrib.auth.decorators import login_required

app_name = 'notebooks'


urlpatterns = [
    url(r'^index',login_required(views.index.as_view()), name = 'index'),
    url(r'^(?P<note_id>[0-9]+)/detail/$', login_required(views.detail), name = 'detail'),
    url(r'^(?P<note_id>[0-9]+)/delete/$', login_required(views.NoteDelete.as_view()), name = 'delete'),
    url(r'^(?P<note_id>[0-9]+)/edit/$', login_required(views.NoteEdit.as_view(model=Note, success_url="/notebooks/index")), name = 'edit'),
    url(r'^create/$', login_required(views.NoteCreate.as_view(model=Note, success_url="/notebooks/index")), name = 'create'),
]
