from django.contrib import messages
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import Record


def record(request):
    if request.method == "POST":
        audio_file = request.FILES.get("recorded_audio")
        language = request.POST.get("language")
        record = Record.objects.create(language=language, voice_record=audio_file)
        record.save()
        messages.success(request, "Audio recording successfully added!")

        return JsonResponse({"success": True})

    context = {"page_title": "Record_audio"}

    return render(request, "voice_recorder/record.html", context)


def record_detail(request, id):
    record = get_object_or_404(Record, id=id)
    context = {
        "page_title": "Record audio detail",
        "record": record,
    }

    return render(request(request, "voice_recorder/record_detail.html", context))


def index(request):
    records = Record.objects.all()
    context = {"page_title": "Voice records", "records": records}

    return render(request, "voice_recorder/index.html", context)
