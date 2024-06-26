from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.conf import settings
import json
from pytube import YouTube
import os
import assemblyai as aai
# import openai
from .models import BlogPost
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context



@login_required
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def generate_blog(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            yt_link = data['link']
        except (KeyError, json.JSONDecodeError):
            return JsonResponse({'error': 'Invalid data sent'}, status=400)

        try:
            # Get YouTube title
            title = yt_title(yt_link)

            # Get transcription
            transcription = get_transcription(yt_link)
            if not transcription:
                return JsonResponse({'error': "Failed to get transcript"}, status=500)

            # Save blog article to database
            new_blog_article = BlogPost.objects.create(
                user=request.user,
                youtube_title=title,
                youtube_link=yt_link,
                generated_content=transcription,
            )
            new_blog_article.save()

            # Return blog article content as a response
            return JsonResponse({'content': transcription})

        except Exception as e:
            # Log the exception for debugging purposes
            print(f"Exception occurred in generate_blog: {str(e)}")
            return JsonResponse({'error': str(e)}, status=500)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


def yt_title(link):
    yt = YouTube(link)
    title = yt.title
    return title

def download_audio(link):
    yt = YouTube(link)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=settings.MEDIA_ROOT)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    return new_file

def get_transcription(link):
    audio_file = download_audio(link)
    aai.settings.api_key = "98102d012dd7413d95a3d73bef8f2e11"

    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(audio_file)

    return transcript.text

def blog_list(request):
    blog_articles = BlogPost.objects.filter(user=request.user)
    return render(request, "all-blogs.html", {'blog_articles': blog_articles})

def blog_details(request, pk):
    blog_article_detail = BlogPost.objects.get(id=pk)
    if request.user == blog_article_detail.user:
        return render(request, 'blog-details.html', {'blog_article_detail': blog_article_detail})
    else:
        return redirect('/')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error_message = "Invalid username or password"
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')

def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeatPassword = request.POST['repeatPassword']

        if password == repeatPassword:
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
                login(request, user)
                return redirect('/')
            except:
                error_message = 'Error creating account'
                return render(request, 'signup.html', {'error_message':error_message})
        else:
            error_message = 'Password do not match'
            return render(request, 'signup.html', {'error_message':error_message})

    return render(request, 'signup.html')

def user_logout(request):
    logout(request)
    return redirect('/')
