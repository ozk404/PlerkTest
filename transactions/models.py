# Librerias externas
import uuid

# Librearias Django
from django.db import models
from django.db.models import Count
from django.db.models.functions import TruncDate


class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name="Name", max_length=200)
    status = models.BooleanField(verbose_name="Status", default=True)

    def top_transaction_date(self):
        date = (
            self.transaction_set.values("trans_date")
            .annotate(r_trans_date=TruncDate("trans_date"))
            .values("r_trans_date")
            .annotate(c_trans_date=Count("r_trans_date"))
            .order_by("-c_trans_date")[0]
            .get("r_trans_date")
        )
        return date

    def total_charged_transactions(self):
        return self.transaction_set.filter(company_id=self.id, aprobation=True).count()

    def total_no_charged_transactions(self):
        return self.transaction_set.filter(company_id=self.id, aprobation=False).count()

    def total_transactions(self):
        return self.transaction_set.filter().all().count()

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name


class TransactionStates(models.TextChoices):
    closed = "closed", "CLOSED"  # -> Transaccion cobrada
    reversed = (
        "reserved",
        "RESERVED",
    )  # -> Cobro realizado y regresado (para validar tarjeta)
    pending = "pending", "PENDING"  # -> Pendiente de cobrar


class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.DecimalField(verbose_name="Price", max_digits=10, decimal_places=2)
    trans_date = models.DateTimeField(
        verbose_name="Date", auto_now=False, auto_now_add=False
    )
    trans_status = models.CharField(
        verbose_name="Status Transaction",
        choices=TransactionStates.choices,
        default=TransactionStates.pending,
        max_length=20,
    )
    aprobation = models.BooleanField(verbose_name="Status Approved", default=False)
    # aprobation -> Uso del Aprobation Status: (false: no se hizo un cobro, true: el cobro si fue aplicado a la tarjeta )
    final_charge = models.BooleanField(verbose_name="Final Charge", default=False)
    company_id = models.ForeignKey(
        Company, verbose_name="Company ID", on_delete=models.PROTECT
    )

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
