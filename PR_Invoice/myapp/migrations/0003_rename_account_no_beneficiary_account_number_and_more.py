# Generated by Django 5.0.1 on 2024-08-28 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_vendor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='beneficiary',
            old_name='account_no',
            new_name='account_number',
        ),
        migrations.RemoveField(
            model_name='beneficiary',
            name='cheque_date',
        ),
        migrations.RemoveField(
            model_name='beneficiary',
            name='cheque_no',
        ),
        migrations.RemoveField(
            model_name='beneficiary',
            name='invoice_date',
        ),
        migrations.RemoveField(
            model_name='beneficiary',
            name='invoice_no',
        ),
        migrations.RemoveField(
            model_name='beneficiary',
            name='issuing_bank',
        ),
        migrations.RemoveField(
            model_name='beneficiary',
            name='material_indent',
        ),
        migrations.RemoveField(
            model_name='beneficiary',
            name='profarma',
        ),
        migrations.RemoveField(
            model_name='beneficiary',
            name='project',
        ),
        migrations.RemoveField(
            model_name='beneficiary',
            name='purchase_order',
        ),
        migrations.RemoveField(
            model_name='beneficiary',
            name='requisition',
        ),
        migrations.AlterField(
            model_name='beneficiary',
            name='pr_no',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='beneficiary',
            name='upi_id',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
