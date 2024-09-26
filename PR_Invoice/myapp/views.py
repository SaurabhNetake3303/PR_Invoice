from django.shortcuts import render, redirect, get_object_or_404
from myapp.form import BeneficiaryForm
from .models import Beneficiary, PR_Request
from django.http import JsonResponse
from django.http import HttpResponse
from datetime import datetime
from django.core.exceptions import ValidationError


# Create your views here.
def Payment_recommendation(request):
    beneficiaryData = Beneficiary.objects.all()
    data = {
        'beneficiaryData': beneficiaryData
    }
    return render(request, "Payment-recommendation.html", data)


def select_beneficiary(request):
    form = BeneficiaryForm()
    return render(request, 'select_beneficiary.html', {'form': form})


def get_beneficiary_details(request):
    beneficiary_id = request.GET.get('beneficiary_id')
    beneficiary = get_object_or_404(Beneficiary, id=beneficiary_id)
    data = {
        'beneficiary_name': beneficiary.beneficiary_name,
        'address': beneficiary.address,
        'pr_no': beneficiary.pr_no,
        'pr_date': beneficiary.pr_date,
        'gstin': beneficiary.gstin,
        'mobile': beneficiary.mobile,
        'email': beneficiary.email,
        'aadhaar': beneficiary.aadhaar,
        'account_holder': beneficiary.account_holder,
        'account_number': beneficiary.account_number,
        'ifsc_code': beneficiary.ifsc_code,
        'bank_name': beneficiary.bank_name,
        'branch': beneficiary.branch,
        'upi_id': beneficiary.upi_id,
        'pan': beneficiary.pan,
    }
    return JsonResponse(data)


def pdf_generate(request):
    return render(request, 'pdf_generate.html')


def pr_request_data(request):
    if request.method == "POST":
        beneficiary_name = request.POST.get("beneficiary_name", "")
        address = request.POST.get("address", "")
        invoice_no = request.POST.get("invoice_no", "")
        proforma = request.POST.get("proforma", "")

        # Ensure purchase_order is a string if the model expects a string
        purchase_order = request.POST.get("purchase_order", "0")

        pr_no = request.POST.get("pr_no", "")
        requisition = request.POST.get("requisition", "")
        material_indent = request.POST.get("material_indent", "")
        project = request.POST.get("project", "")
        gstin = request.POST.get("gstin", "")
        mobile = request.POST.get("mobile", "")
        pan = request.POST.get("pan", "")
        email = request.POST.get("email", "")
        adhaar = request.POST.get("adhaar", "")

        # Bank Details
        account_holder = request.POST.get("account_holder", "")
        account_number = request.POST.get("account_number", "")
        ifsc_code = request.POST.get("ifsc_code", "")
        bank_name = request.POST.get("bank_name", "")
        branch = request.POST.get("branch", "")
        upi_id = request.POST.get("upi_id") or None

        invoice_date = request.POST.get("invoice_date", "")
        pr_date = request.POST.get("pr_date", "")
        check_date = request.POST.get("check_date", "")


        # Financial Details
        subtotal = float(request.POST.get("subtotal", 0) or 0)
        cgst = float(request.POST.get("cgst", 0) or 0)
        sgst = float(request.POST.get("sgst", 0) or 0)
        tds = float(request.POST.get("tds", 0) or 0)
        retention = float(request.POST.get("retention", 0) or 0)
        advance = float(request.POST.get("advance", 0) or 0)
        debit_note = float(request.POST.get("debit_note", 0) or 0)
        round_off = float(request.POST.get("round_off", 0) or 0)
        net_payable = float(request.POST.get("net_payable", 0) or 0)

        # Validate check_no
        check_no_str = request.POST.get("check_no", "").strip()
        check_no = None
        if check_no_str:
            try:
                check_no = int(check_no_str)
                if check_no < 0:
                    raise ValidationError("Check number cannot be negative.")
            except ValueError:
                raise ValidationError("Check number must be a valid integer.")

        # Create and save the PR_Request object
        s = PR_Request(
            beneficiary_name=beneficiary_name,
            address=address,
            invoice_no=invoice_no,
            invoice_date=invoice_date,
            proforma=proforma,
            purchase_order=purchase_order,
            pr_no=pr_no,
            pr_date=pr_date,
            requisition=requisition,
            material_indent=material_indent,
            project=project,
            gstin=gstin,
            mobile=mobile,
            pan=pan,
            email=email,
            adhaar=adhaar,
            account_holder=account_holder,
            account_number=account_number,
            ifsc_code=ifsc_code,
            bank_name=bank_name,
            branch=branch,
            upi_id=upi_id,
            subtotal=subtotal,
            cgst=cgst,
            sgst=sgst,
            tds=tds,
            retention=retention,
            advance=advance,
            debit_note=debit_note,
            round_off=round_off,
            net_payable=net_payable,
            check_no=check_no,
            check_date=check_date
        )
        s.save()

        return redirect("pdf_generate")

    else:
        # Redirect back or render a form if the method is not POST
        return redirect("select_beneficiary")


