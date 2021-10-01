# coding:utf-8

from django.shortcuts import redirect, reverse
from django.views.generic import View
from app.models import Comment
from django.http import JsonResponse


class Comments(View):
    def get(self, request, comment_id, video_id):
        comment = Comment.objects.get(pk=comment_id)

        comment.status = not comment.status
        comment.save()

        return redirect(reverse('video_sub', kwargs={'video_id': video_id}))

