# coding:utf-8

from django.shortcuts import redirect, reverse
from django.views.generic import View
from app.libs.base_render import render_to_response
from app.utils.permission import dashboard_auth
from app.utils.common import check_and_get_video_type
from app.model.video import VideoType, FromType, NationalityType, Video


class ExternaVideo(View):
    TEMPLATE = 'dashboard/video/externa_video.html'

    @dashboard_auth
    def get(self, request):

        error = request.GET.get('error', '')
        data = {'error': error}

        video =Video.objects.exclude(from_to=FromType.custom.value)
        data['video'] = video

        return render_to_response(request, self.TEMPLATE, data)

    def post(self, request):

        name = request.POST.get('name')
        image = request.POST.get('image')
        video_type = request.POST.get('video_type')
        from_to = request.POST.get('from_to')
        nationality = request.POST.get('nationality')
        info = request.POST.get('info')

        if not all([name, image, video_type, from_to, nationality, info]):
            return redirect('{}?error={}'.format(reverse('externa_video'), '缺少必要字段'))

        result = check_and_get_video_type(VideoType, video_type, '非法的视频类型')
        if result.get('code') != 0:
            return redirect('{}?error={}'.format(reverse('externa_video'), result['msg']))

        result = check_and_get_video_type(FromType, from_to, '非法的来源')
        if result.get('code') != 0:
            return redirect('{}?error={}'.format(reverse('externa_video'), result['msg']))

        result = check_and_get_video_type(NationalityType, nationality, '非法的国家')
        if result.get('code') != 0:
            return redirect('{}?error={}'.format(reverse('externa_video'), result['msg']))

        Video.objects.create(
            name=name,
            image=image,
            video_type=video_type,
            from_to=from_to,
            nationality=nationality,
            info=info
        )


        return redirect(reverse('externa_video'))
