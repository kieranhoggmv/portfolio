from pprint import pprint
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from docx import Document

KSBS = {
    "K1": {"paragraphs": []},
    "K2": {"paragraphs": []},
    "K5": {"paragraphs": []},
    "K6": {"paragraphs": []},
    "K7": {"paragraphs": []},
    "K10": {"paragraphs": []},
    "K13": {"paragraphs": []},
    "K14": {"paragraphs": []},
    "K15": {"paragraphs": []},
    "S5": {"paragraphs": []},
    "S9": {"paragraphs": []},
    "S10": {"paragraphs": []},
    "S11": {"paragraphs": []},
    "S13": {"paragraphs": []},
    "S14": {"paragraphs": []},
    "B1": {"paragraphs": []},
    "B2": {"paragraphs": []},
    "B5": {"paragraphs": []},
    "B6": {"paragraphs": []},
    "B7": {"paragraphs": []},
}


class Home(TemplateView):
    template_name = "upload.html"

    def post(self, request, *args, **kwargs):
        document = Document(request.FILES["file"].file)
        previous_paragraph = None
        for i, paragraph in enumerate(document.paragraphs):
            for key in KSBS:
                if f"[{key}]" in paragraph.text or f"({key})" in paragraph.text:
                    if previous_paragraph:
                        KSBS[key]["paragraphs"].append(previous_paragraph.text)
                    KSBS[key]["paragraphs"].append(paragraph.text)
                    # print(paragraph.text)
            previous_paragraph = paragraph
        pprint(KSBS)
        return JsonResponse(KSBS)
