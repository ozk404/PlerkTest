from django.forms import CharField
from rest_framework import serializers
from .models import Company, Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class CompanySalesSerializer(serializers.Serializer):
    name = serializers.CharField()
    total_charged_transactions = serializers.IntegerField()
    total_no_charged_transactions = serializers.IntegerField()
    top_transaction_date = serializers.DateTimeField()


class SummarySerializer(serializers.Serializer):
    top_company_name = serializers.CharField()
    top_transaction_company_id = serializers.UUIDField()
    top_transactions_company = serializers.IntegerField()
    least_company_name = serializers.CharField()
    least_transactions_company = serializers.UUIDField()
    least_transactions = serializers.IntegerField()
    total_closed_transactions_price = serializers.IntegerField()
    total_pending_transactions_price = serializers.IntegerField()
    total_non_approved_transacions = serializers.IntegerField()
    non_approved_company_name = serializers.CharField()
    non_approved_company_id = serializers.UUIDField()
    non_approved_company_transactions = serializers.IntegerField()


class CompanyServiceSerialize(serializers.Serializer):
    name = serializers.CharField()
    id = serializers.UUIDField()
    total_charged_transactions = serializers.IntegerField()
    total_no_charged_transactions = serializers.IntegerField()
    top_transaction_date = serializers.DateField()
