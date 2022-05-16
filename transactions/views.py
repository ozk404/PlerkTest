from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.db.models import Count, Sum

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Transaction, Company
from .serializers import CompanySerializer,CompanyServiceSerialize, SummarySerializer
from transactions import serializers

class CompanyData(APIView):
    
    def get(self, request):
        company = Company.objects.all()
        copmanu_serializer = CompanySerializer(company, many=True)
        return Response(copmanu_serializer.data, status=status.HTTP_200_OK)


def check_transactions(status):
    trans = Transaction.objects.filter(trans_status=f"{status}").values()
    total_paid_transactions = 0
    for trans in list(trans):
        total_paid_transactions += int(trans["price"])
    return total_paid_transactions


def check_company_transactions_price(company):
    trans = Transaction.objects.filter(
        company_id=company, trans_status="closed"
    ).values()
    total_paid_transactions = 0
    for trans in list(trans):
        total_paid_transactions += int(trans["price"])
    return total_paid_transactions


class SummaryService(APIView):
    def get(self, request):
        company_transactions = (
            Transaction.objects.values_list("company_id")
            .annotate(company_count=Count("company_id"))
            .order_by("-company_count")
        )
        top_transaction_company_id = list(company_transactions)[0][0]
        top_company = Company.objects.get(pk=top_transaction_company_id)
        top_transactions_company = Company.total_transactions(top_company)
        top_company_name = top_company.name

        least_transactions_company = list(company_transactions)[
            company_transactions.count() - 1
        ][0]
        least_transactions = list(company_transactions)[
            company_transactions.count() - 1
        ][1]
        least_company_name = (
            Company.objects.filter(id=least_transactions_company)
        ).values()[0]["name"]

        total_closed_transactions_price = check_transactions("closed")
        total_pending_transactions_price = check_transactions("pending")

        total_non_approved_transacions = Transaction.objects.filter(aprobation=False)
        non_approved_transacions = company_transactions.filter(aprobation=False)
        non_approved_company_id = list(non_approved_transacions)[0][0]
        non_approved_company = Company.objects.get(pk=non_approved_company_id)
        non_approved_company_transactions = Company.total_no_charged_transactions(non_approved_company)
        non_approved_company_name = (
            Company.objects.filter(pk=non_approved_company_id)
        ).values()[0]["name"]

        summary_serializer = SummarySerializer(
            data={
                "top_company_name": top_company_name,
                "top_transaction_company_id": top_transaction_company_id,
                "top_transactions_company": top_transactions_company,
                "least_company_name": least_company_name,
                "least_transactions_company": least_transactions_company,
                "least_transactions": least_transactions,
                "total_closed_transactions_price": total_closed_transactions_price,
                "total_pending_transactions_price": total_pending_transactions_price,
                "total_non_approved_transacions": total_non_approved_transacions.count(),
                "non_approved_company_name": non_approved_company_name,
                "non_approved_company_id": non_approved_company_id,
                "non_approved_company_transactions": non_approved_company_transactions,
            }
        )
        if summary_serializer.is_valid():
            return Response(summary_serializer.data, status=status.HTTP_200_OK)
        return Response(summary_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyService(APIView):
    def get(self, request, company_id):
        company = Company.objects.get(pk=company_id)
        total_charged_transactions = Company.total_charged_transactions(company)
        total_no_charged_transactions = Company.total_no_charged_transactions(company)
        top_date = Company.top_transaction_date(company)
        company_serializer = CompanyServiceSerialize(
            data={
                "name": company.name,
                "id": company.id,
                "total_charged_transactions": total_charged_transactions,
                "total_no_charged_transactions": total_no_charged_transactions,
                "top_transaction_date": top_date,
            }
        )
        if company_serializer.is_valid():
            return Response(company_serializer.data, status=status.HTTP_200_OK)
        return Response(company_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TopCompanies(APIView):
    def get(self, request, top_entries =10):
        tp = {}
        company_transactions = (
            Transaction.objects.values_list("company_id")
            .annotate(company_count=Count("company_id"))
            .order_by("-company_count")
        )
        top_transaction_company_id = list(company_transactions)[:top_entries]
        for i in top_transaction_company_id:
            company = Company.objects.get(pk=i[0])
            tp[str(i[0])] = {
                "Name": company.name,
                "Total Transactions": Company.total_transactions(company),
                "Total Charged Transactions": Company.total_charged_transactions(company),
                "Total Revenue" :  check_company_transactions_price(company.id),
            }

        return Response(tp, status=status.HTTP_200_OK)
