from django.shortcuts import render
from study.models import Study


def download(request):
    study_python = Study.objects.all()
    context = {
        'study_list':study_python
    }

    return render(request, 'study/download.html', context)
