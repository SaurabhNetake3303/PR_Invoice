from django.db import models

from datetime import datetime
# Create your models here.
# myapp/models.py


class Beneficiary(models.Model):
    beneficiary_name = models.CharField(max_length=255)
    address = models.TextField()
    pr_no = models.CharField(max_length=100)
    pr_date = models.DateField()
    gstin = models.CharField(max_length=15)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    aadhaar = models.CharField(max_length=12)
    account_holder = models.CharField(max_length=255)
    account_number = models.CharField(max_length=20)
    ifsc_code = models.CharField(max_length=11)
    bank_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    upi_id = models.CharField(max_length=50)
    pan = models.CharField(max_length=10)

    def __str__(self):
        return self.beneficiary_name


class PR_Request(models.Model):
    beneficiary_name = models.CharField(max_length=255, default="")
    address = models.TextField(max_length=255, default="")
    invoice_no = models.PositiveIntegerField(default=0)
    invoice_date = models.DateField()
    proforma = models.CharField(max_length=255, default="")
    purchase_order = models.PositiveIntegerField(default=0)
    pr_no = models.PositiveIntegerField(default=0)
    pr_date = models.DateField()
    # time = datetime.now()
    # pr_date = time.strftime("%Y-%m-%d")

    requisition = models.CharField(max_length=255, default="")
    material_indent = models.CharField(max_length=255, default="")
    project = models.CharField(max_length=255, default="")
    gstin = models.CharField(max_length=15, default="")
    mobile = models.CharField(max_length=15, default="")
    pan = models.CharField(max_length=10, default="")
    email = models.EmailField(max_length=50, default="")
    adhaar = models.CharField(max_length=12, default="")

    # Bank Details
    account_holder = models.CharField(max_length=255, default="")
    account_number = models.CharField(max_length=20, default="")
    ifsc_code = models.CharField(max_length=11, default="")
    bank_name = models.CharField(max_length=255, default="")
    branch = models.CharField(max_length=255, default="")
    upi_id = models.CharField(max_length=255, default="")

    # Financial Details
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    cgst = models.DecimalField(max_digits=10, decimal_places=2)
    sgst = models.DecimalField(max_digits=10, decimal_places=2)
    tds = models.DecimalField(max_digits=10, decimal_places=2)
    retention = models.DecimalField(max_digits=10, decimal_places=2)
    advance = models.DecimalField(max_digits=10, decimal_places=2)
    debit_note = models.DecimalField(max_digits=10, decimal_places=2)

    # Make check_date nullable and blank
    check_no = models.IntegerField(null=True, blank=True)
    check_date = models.DateField(null=True, blank=True)

    round_off = models.DecimalField(max_digits=10, decimal_places=2)
    net_payable = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "myapp_pr_request"
