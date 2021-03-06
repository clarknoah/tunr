from django.shortcuts import render, redirect

from .models import Artist, Song
from .forms import ArtistForm, SongForm
from django.views import View
from rest_framework import generics
from .serializers import ArtistSerializer

# Create your views here.

class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    #serializer_class = SongSerializer

def songs_list(request):
    songs = Song.objects.all()
    return render(request, 'tunr/songs_list.html', {'songs':songs})

def song_detail(request, pk):
    song = Song.objects.get(id=pk)
    return render(request, 'tunr/song_detail.html', {'song':song})



#
# class ArtistList(View):
#     def get(self, request):
#         artists = Artist.objects.all()
#         return render(request, 'tunr/artist_list.html', { 'artists': artists })
#
#
# class ArtistCreate(View):
#     def get(self,request):
#         form = ArtistForm()
#         return render(request, 'tunr/artist_form.html', { 'form' : form })
#
#     def post(self,request):
#         form = ArtistForm(request.POST)
#         if form.is_valid():
#             artist = form.save()
#             return redirect('artist_detail', pk=artist.pk)
#
#
#
#
#
# def artist_list(request):
#     artists = Artist.objects.all()
#     return render(request, 'tunr/artist_list.html', { 'artists': artists })
#
# def artist_detail(request, pk):
#     artist = Artist.objects.get(id=pk)
#     return render(request, 'tunr/artist_detail.html', { 'artist': artist })
#
# def artist_create(request):
#     if request.method == 'POST':
#         form = ArtistForm(request.POST)
#         if form.is_valid():
#             artist = form.save()
#             return redirect('artist_detail', pk=artist.pk)
#     else:
#         form = ArtistForm()
#     return render(request, 'tunr/artist_form.html', { 'form' : form })
#
# def artist_edit(request, pk):
#     artist = Artist.objects.get(id=pk)
#     if request.method == 'POST':
#         form = ArtistForm(request.POST, instance=artist)
#         if form.is_valid():
#             artist = form.save()
#             return redirect('artist_detail', pk=artist.pk)
#     else:
#         form = ArtistForm(instance=artist)
#     return render(request, 'tunr/artist_form.html', { 'form': form })
#
# def artist_delete(request, pk):
#     Artist.objects.get(id=pk).delete()
#     return redirect('artist_list')
#
#

# def song_create(request):
#     if request.method == 'POST':
#         form = SongForm(request.POST)
#         if form.is_valid():
#             song = form.save()
#             return redirect('song_detail', pk=song.pk)
#     else:
#         form = SongForm()
#     return render(request, 'tunr/song_form.html', { 'form' : form })
#
#


# def song_edit(request, pk):
#     song = Song.objects.get(id=pk)
#     if request.method == 'POST':
#         form = SongForm(request.POST, instance=song)
#         if form.is_valid():
#             song = form.save()
#             return redirect('song_detail', pk=song.pk)
#     else:
#         form = SongForm(instance=song)
#     return render(request, 'tunr/song_form.html', { 'form': form })
#
# def song_delete(request, pk):
#     Song.objects.get(id=pk).delete()
#     return redirect('artist_list')
