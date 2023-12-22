"""Views"""
# import io
from django.http import HttpResponse
from django.shortcuts import render
from pytube import YouTube
from pytube.exceptions import VideoUnavailable


def download_video(request):
    if request.method == 'POST':
        video_url = request.POST.get('url')
        format_requested = request.POST.get('format')

        if format_requested == 'mp4':
            try:
                yt = YouTube(video_url)
                stream = yt.streams.get_highest_resolution()
            except VideoUnavailable:
                return HttpResponse('The video is unavailable')
            except Exception as error:
                return HttpResponse(f'An error occurred: {str(error)}')

            response = HttpResponse(content_type='video/mp4')
            response['Content-Disposition'] = f'attachment; filename="{yt.title}.mp4"'
            stream.stream_to_buffer(response)
            return response

        if format_requested == 'mp3':
            try:
                yt = YouTube(video_url)
                stream = yt.streams.filter(only_audio=True).first()
            except VideoUnavailable:
                return HttpResponse('The video is unavailable')
            except Exception as error:
                return HttpResponse(f'An error occurred: {str(error)}')

            response = HttpResponse(content_type='audio/mpeg')
            response['Content-Disposition'] = f'attachment; filename="{yt.author} - {yt.title}.mp3"'
            stream.stream_to_buffer(response)
            return response

    return render(request, 'downloader/download.html')


def home(request):
    try:
        return render(request, 'downloader/index.html')
    except Exception as error:
        return HttpResponse(f'An error occurred: {str(error)}')

# ###### WORKING BEFORE

# def download_video(request):
#     if request.method == 'POST':
#         video_url = request.POST.get('url')
#         try:
#             yt = YouTube(video_url)
#             stream = yt.streams.get_highest_resolution()
#         except VideoUnavailable:
#             return HttpResponse("The video is unavailable")
#         except Exception as e:
#             return HttpResponse("An error occurred: {}".format(str(e)))
#         else:
#             response = HttpResponse(stream.stream_to_buffer(), content_type='video/mp4')
#             response['Content-Disposition'] = 'attachment; filename="{}.mp4"'.format(yt.title)
#             response['Content-Length'] = response.tell()
#             request.session['video_title'] = yt.title
#             return redirect('download')

#     return render(request, 'downloader/index.html')

# def download(request):
#     video_title = request.session.get('video_title')
#     if video_title is None:
#         return redirect('index')
#     else:
#         del request.session['video_title']
#         return HttpResponse(render_to_string('downloader/download.html', {'video': {'title': video_title}}))

# ######

# def download_video(request):
#     if request.method == 'POST':
#         video_url = request.POST.get('url')
#         try:
#             yt = YouTube(video_url)
#             stream = yt.streams.get_highest_resolution()
#         except VideoUnavailable:
#             return HttpResponse("The video is unavailable")
#         except Exception as e:
#             return HttpResponse("An error occurred: {}".format(str(e)))
#         else:
#             response = HttpResponse(content_type='video/mp4')
#             response['Content-Disposition'] = 'attachment; filename="{}.mp4"'.format(yt.title)
#             stream.stream_to_buffer(response)
#             return render(request, 'downloader/download.html', {'video': response})
#     else:
#         return render(request, 'downloader/index.html')


# def download_video(request):
#     if request.method == 'POST':
#         url = request.POST['url']
#         try:
#             yt = YouTube(url)
#             stream = yt.streams.get_highest_resolution()
#             stream.download()
#             return render(request, 'download.html')
#         except VideoUnavailable:
#             return render(request, 'error.html', {'error': 'Video unavailable'})
#     else:
#         return render(request, 'index.html')
