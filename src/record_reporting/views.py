import io
import os
from django.http import FileResponse
from django.shortcuts import render
from docxtpl import DocxTemplate
from django.contrib.auth.decorators import login_required


@login_required
def add_report(request):
    return render(request, "record_reporting/add-report.html", {})


@login_required
def list_report(request):
    return render(request, "record_reporting/list-report.html", {})


@login_required
def submit_report(request):
    report = DocxTemplate(os.path.join("templates/record_reporting", 'record_reporting.docx'))

    context = {
        'court_case_applicants': request.GET.get('court_case_applicants'),
        'bailiff_name': request.GET.get('bailiff_name'),
        'court_case_num': request.GET.get('court_case_num'),
        'bailiff_address': request.GET.get('bailiff_address'),
        'court_case_date': request.GET.get('court_case_date'),
        'court_case_time': request.GET.get('court_case_time'),
        'court_case_msg_title': request.GET.get('court_case_msg_title'),
        'court_case_lawyer': request.GET.get('court_case_lawyer'),
        'court_case_agent': request.GET.get('court_case_agent'),
        'court_case_defendants': request.GET.get('court_case_defendants'),
        'court_case_msg_content': request.GET.get('court_case_msg_content'),

    }
    report.render(context)
    report_io = io.BytesIO()
    report.save(report_io)
    report_io.seek(0)
    return FileResponse(report_io, as_attachment=True, filename=f'reporting_generated.docx')


@login_required
def search_report(request):
    return render(request, "", {})
