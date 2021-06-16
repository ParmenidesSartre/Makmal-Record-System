from django.shortcuts import render, get_object_or_404, redirect
from .models import Report
from django.contrib.auth.decorators import login_required
from .forms import ReportForm, AddRecordForm
from .render import Render


def index(request):
    return render(request, 'pages/index.html')

@login_required
def makmal(request):
    # Obtain all record from database
    reports = Report.objects.order_by('-done_on')

    context = {
        'reports': reports
    }

    return render(request, 'makmal/strelise.html', context )

@login_required
def edit_report(request, pk):
    report = get_object_or_404(Report, id=pk)
    if request.method == "POST":
        form = ReportForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            return redirect('makmal')
        else:
            print(form.errors)
            return redirect('editreport')
    else:
        form = ReportForm(instance=report)

    context = {
        'form': form, 'file': report
    }

    return render(request, 'makmal/editrecord.html', context )

@login_required
def add_record(request):
    if request.method == "POST":
        form = AddRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('makmal')
    else:
        form = AddRecordForm()
    
    context = {
        'form' : form
    }

    return render(request, 'makmal/addrecord.html', context )

@login_required
def print_report(request, pk):
    report = get_object_or_404(Report, id=pk)
    form = ReportForm(instance=report)

    context = {
        'form': form,
        'request': request
    }

    return Render.render('makmal/stereliseform.html', context )
