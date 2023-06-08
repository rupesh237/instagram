from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

import requests


def instagram_feed(request):
    params={
        'fields': 'id, caption, media_type, media_url, permalink, thumbnail_url, timestamp'
    }
    access_token = 'IGQVJVWHVfV0tNSEprWjZANeldVZAGdMUU4zNWg3T2xGX0tRakJTaC1hT3VkZADE5SGoxSTdQWXFpXzdlZA1ZAkLTE5Wi1BVC1Cek5VRjVHRHJiX1hlUHBnYS1BY1hyMUNPVDl3NFgtVjhVTXdYMmdjWnlLZAQZDZD'
    url = f'https://graph.instagram.com/me/media?access_token={access_token}'
    response = requests.get(url, params=params)
    print(response)
    data = response.json()
    # print(data)
    if 'error' in data:
        # Handle any errors that occurred
        return render(request, 'error.html', {'message': data['error']['message']})
    photos = []
    for item in data['data']:
        # print(item)
        photo = {
            'url': item['permalink'] if 'permalink' in item else '',
            'caption': item['caption'] if 'caption' in item else '',
            'likes': item['like_count'] if 'like_count' in item else '',
            'comments': item['comments_count'] if 'comments_count' in item else '',
            'image_url': item['media_url'] if 'media_url' in item else '',
            'image_tag': f'<img src="{item["media_url"]}" alt="{item["caption"] if "caption" in item else ""}">' if 'media_url' in item else '',
        }
        photos.append(photo)
    context = {'photos': photos}
    return render(request, 'api_data_fetch/instagram_feed.html', context)
    # return HttpResponse(photos)





# def instagram_feed(request):
#     access_token = 'IGQVJVWHVfV0tNSEprWjZANeldVZAGdMUU4zNWg3T2xGX0tRakJTaC1hT3VkZADE5SGoxSTdQWXFpXzdlZA1ZAkLTE5Wi1BVC1Cek5VRjVHRHJiX1hlUHBnYS1BY1hyMUNPVDl3NFgtVjhVTXdYMmdjWnlLZAQZDZD'
#     url = f'https://api.instagram.com/v1/users/self/media/recent/?access_token={access_token}'
#     response = requests.get(url)
#     data = response.json()
#     photos = []
#     for item in data['data']:
#         photo = {
#             'url': item['images']['standard_resolution']['url'],
#             'caption': item['caption']['text'] if item['caption'] else '',
#             'likes': item['likes']['count'],
#             'comments': item['comments']['count']
#         }
#         photos.append(photo)
#     context = {'photos': photos}
#     return render(request, 'instagram_feed.html', context)

# def instagram_feed(request):
#     access_token = 'IGQVJVWHVfV0tNSEprWjZANeldVZAGdMUU4zNWg3T2xGX0tRakJTaC1hT3VkZADE5SGoxSTdQWXFpXzdlZA1ZAkLTE5Wi1BVC1Cek5VRjVHRHJiX1hlUHBnYS1BY1hyMUNPVDl3NFgtVjhVTXdYMmdjWnlLZAQZDZD'
#     url = f'https://api.instagram.com/v1/users/self/media/recent/?access_token={access_token}'
#     response = requests.get(url)
#     data = response.json()
#     photos = []
#     for item in data['data']:
#         photo = {
#             'url': item['images']['standard_resolution']['url'],
#             'caption': item['caption']['text'] if item['caption'] else '',
#             'likes': item['likes']['count'],
#             'comments': item['comments']['count']
#         }
#         photos.append(photo)
#     context = {'photos': photos}
#     return render(request, 'instagram_feed.html', context)

# def instagram_feed(request):
#     access_token = 'IGQVJVWHVfV0tNSEprWjZANeldVZAGdMUU4zNWg3T2xGX0tRakJTaC1hT3VkZADE5SGoxSTdQWXFpXzdlZA1ZAkLTE5Wi1BVC1Cek5VRjVHRHJiX1hlUHBnYS1BY1hyMUNPVDl3NFgtVjhVTXdYMmdjWnlLZAQZDZD'
#     url = f'https://api.instagram.com/v1/users/self/media/recent/?access_token={access_token}'
#     response = requests.get(url)
#     data = response.json()
#     photos = []
#     for item in data['data']:
#         photo = {
#             'url': item['images']['standard_resolution']['url'],
#             'caption': item['caption']['text'] if item['caption'] else '',
#             'likes': item['likes']['count'],
#             'comments': item['comments']['count']
#         }
#         photos.append(photo)
#     context = {'photos': photos}
#     return render(request, 'instagram_feed.html', context)
