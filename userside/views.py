from django.shortcuts import render, redirect
from . models import IncidentReport, SubIncidentTypes
from django.contrib import messages

# Create your views here.


def SubmitForm(request):
    if request.method != 'POST':
        return render(request, 'ReportingForm.html')
    try:
        user = request.user
        location = request.POST["location"]
        department = request.POST["department"]
        date = request.POST["date"]
        time = request.POST["time"]
        incident_location = request.POST["incident_location"]
        initial_severity = request.POST["initial_severity"]
        suspected_cause = request.POST["suspected_cause"]
        immediate_action = request.POST["immediate_action"]
        sub_incident_type = request.POST.getlist('sub_incident_type')

        data = IncidentReport.objects.create(user=user,location=location, department=department,
                                            date=date, time=time, incident_location=incident_location,
                                            initial_severity=initial_severity,
                                            suspected_cause=suspected_cause, immediate_action=immediate_action)
        data.save()

        for type in sub_incident_type:

            types = SubIncidentTypes(typeof=data)
            types.type = type
            types.save()
        messages.success(request, 'Form Submitted')
        return redirect('home')
    except:
        messages.error(request, 'Please fill all fields')
        return redirect(SubmitForm)



