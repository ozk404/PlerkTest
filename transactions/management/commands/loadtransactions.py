import pandas as pd
import os.path as pt
import os
from django.core.management.base import BaseCommand, CommandError
from transactions.models import Transaction, Company


class Command(BaseCommand):
    def handle(self, *args, **options):
        path = pt.abspath(pt.join( os.getcwd(), os.pardir)) + r"\test_database.csv"
        data = pd.read_csv(
            path
        )
        data["company"] = data["company"].str.capitalize()
        df = pd.DataFrame(
            data,
            columns=[
                "company",
                "price",
                "date",
                "status_transaction",
                "status_approved",
            ],
        )
        df_fixed = (
            df.drop_duplicates().dropna()
        )  # ->  Removemos si hubiera un duplicado exacto de una transaccion
        transactions = []
        try:
            for index, row in df_fixed.iterrows():
                company_name = str(row["company"])
                companyid = Company.objects.get(name__exact=company_name)
                charge = get_final_charge(
                    row["status_transaction"], row["status_approved"]
                )
                price = get_real_price(row["price"])
                transactions.append(
                    Transaction(
                        price=price,
                        trans_date=row["date"],
                        trans_status=row["status_transaction"],
                        aprobation=row["status_approved"],
                        company_id=companyid,
                        final_charge=charge,
                    )
                )
                print("Added new Transaction: ", row["company"], row["date"])
            created = Transaction.objects.bulk_create(transactions)
            total = len(created)
            if not total:
                print("No new companies added in DB")
            else:
                print(total, "New Companies added in DB!")
        except Exception as e:
            print("Eror: ", e)

    # Funcion para saber si la transacción fue aprobada y cumple con los requisitos


def get_final_charge(status_transaction, status_approved):
    if str(status_transaction) == "closed" and status_approved == True:
        charge = True
    else:
        charge = False
    return charge


# Funcion para obtener el precio real
def get_real_price(price):
    real_price = price / 100
    return real_price
