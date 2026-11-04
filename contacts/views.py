from django.http import HttpResponse, QueryDict
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods

from .models import Contact


def contact_list(request):
    return render(request, "contacts/index.html", {
        "name": "Azzam Zawawi Al Rasyid",
        "contacts": Contact.objects.all(),
    })


def contact_add(request):
    if request.method == "POST":
        contact = Contact.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone", ""),
        )
        # Exercises 2 and 3: return the new row and out-of-band feedback.
        return render(request, "contacts/_contact_result.html", {"contact": contact})
    return render(request, "contacts/_contact_rows.html", {"contacts": Contact.objects.all()})


@require_http_methods(["DELETE"])
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return HttpResponse("")


def contact_search(request):
    query = request.GET.get("q", "")
    contacts = Contact.objects.filter(name__icontains=query) if query else Contact.objects.all()
    return render(request, "contacts/_contact_rows.html", {"contacts": contacts})


def contact_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, "contacts/_contact_edit_row.html", {"contact": contact})


def contact_row(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, "contacts/_contact_row.html", {"contact": contact})


@require_http_methods(["PUT"])
def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    data = QueryDict(request.body)
    contact.name = data.get("name", contact.name)
    contact.email = data.get("email", contact.email)
    contact.phone = data.get("phone", contact.phone)
    contact.save()
    return render(request, "contacts/_contact_row.html", {"contact": contact})
