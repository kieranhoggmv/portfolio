from pprint import pprint
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from docx import Document


KSBS = {
    "K1": {},
    "K2": {},
    "K5": {},
    "K6": {},
    "K7": {},
    "K10": {},
    "K13": {},
    "K14": {},
    "K15": {},
    "S5": {},
    "S9": {},
    "S10": {},
    "S11": {},
    "S13": {},
    "S14": {},
    "B1": {},
    "B2": {},
    "B5": {},
    "B6": {},
    "B7": {},
}


class Home(TemplateView):
    template_name = "upload.html"

    def post(self, request, *args, **kwargs):
        PROJECT_STYLE = "Heading 2"
        document = Document(request.FILES["file"].file)
        paragraphs = [
            (para.text, para.style.name.replace(" ", "_"))
            for para in document.paragraphs
        ]
        projects = []
        project = None
        # previous_paragraph = None
        for i, paragraph in enumerate(document.paragraphs):
            for run in paragraph.runs:
                if run.font.italic:
                    print(run.text)
            if paragraph.style.name == PROJECT_STYLE and "#" in paragraph.text:
                if paragraph.text != project:
                    project = paragraph.text
                    projects.append(project)

            for key in KSBS:
                if (
                    f"[{key}]" in paragraph.text
                    or f"({key})" in paragraph.text
                    or f"/{key}" in paragraph.text
                    or f"{key}/" in paragraph.text
                ):
                    # if previous_paragraph:
                    #     KSBS[key]["paragraphs"].append(previous_paragraph.text)
                    if i not in KSBS[key].keys():
                        KSBS[key][i] = paragraph.text, project
            # previous_paragraph = paragraph
        # missing_ksbs = list(filter(lambda x: len(KSBS[x]) == 0, KSBS))
        # met_ksbs = list(filter(lambda x: x not in missing_ksbs, KSBS))
        # pprint(KSBS)
        return render(
            request,
            self.template_name,
            {
                "ksbs": KSBS,
                # "missing_ksbs": missing_ksbs,
                # "met_ksbs": met_ksbs,
                "paragraphs": paragraphs,
            },
        )
