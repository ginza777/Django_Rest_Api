import random
from django.core.management.base import BaseCommand
from faker import Faker
from app.models import CustomUser, CompanyMember, Company
#import atomic transaction
from django.db import transaction

Choice=[
    ('customer','customer'),
    ('admin','admin'),
    ('manager','manager'),
    ('employee','employee'),
    ('teacher','teacher'),
    ('block','block'),
    ('test','test')

]

CompanyMemberRole=[
    ('admin','admin'),
    ('founder','founder'),
    ('employee','employee')
]



class Command(BaseCommand):
    help = "Create fake users"

    def add_arguments(self, parser):
        parser.add_argument("total", type=int, help="Indicates the number of users to be created")

    def handle(self, *args, **kwargs):
        total = kwargs["total"]
        fake = Faker()
        company1, created1 = Company.objects.get_or_create(name='company1')
        company2, created2 = Company.objects.get_or_create(name='company2')
        company3, created3 = Company.objects.get_or_create(name='company3')
        list_company=[company1,company2,company3]

        for i in range(total):
            try:
                user = CustomUser.objects.create(
                    username=fake.name(),
                    email=fake.email(),
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    date_joined=fake.date_time(),
                    phone=fake.phone_number(),
                    privaligies=random.choice(Choice)[0],
                )
                user.save()

                CompanyMember.objects.create(
                    user=user,
                    role='employee',
                    company=random.choice(list_company)
                ).save()
            except:
                continue





            print(f"{i} - {user.username} fake user created {user.phone}")







        print("Fake user created successfully")