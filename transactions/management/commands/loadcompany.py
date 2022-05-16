import pandas as pd
from django.core.management.base import BaseCommand, CommandError
from transactions.models import Company


class Command(BaseCommand):
    def handle(self, *args, **options):
        urlfile = 'https://raw.githubusercontent.com/ozk404/PlerkTest/main/test_database.csv'
        data = pd.read_csv(
            urlfile,sep=",")
        
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
        df_fixed = df.drop_duplicates(
            subset=["company"]
        ).dropna()  # ->  Removemos todas las 'Company' duplicadas
        companies = []
        try:
            for index, row in df_fixed.iterrows():
                company_name = str(row["company"]).capitalize()
                if not Company.objects.filter(name__exact=company_name):
                    print("Added new company: ", company_name)
                    companies.append(Company(name=company_name))
            created = Company.objects.bulk_create(companies)
            total = len(created)
            if not total:
                print("No new companies added in DB")
            else:
                print(total, "New Companies added in DB!")
        except Exception as e:
            print("Eror: ", e)
