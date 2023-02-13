import json
import requests
import subprocess

from django.http import JsonResponse
from .models import Video

def upload_video(request):
    if request.method == 'POST':
        video_file = request.FILES['video']
        video = Video.objects.create(video_file=video_file)

        # Call the deepfake detection script
        result = subprocess.run(['python', '<script_path>', video.video_file.path], stdout=subprocess.PIPE)
        prediction = result.stdout.decode('utf-8').strip()

        return JsonResponse({'success': True, 'prediction': prediction})
    return JsonResponse({'success': False})