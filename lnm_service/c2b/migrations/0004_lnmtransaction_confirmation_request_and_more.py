# Generated by Django 4.0.1 on 2022-02-02 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('c2b', '0003_alter_lnmtransaction_transaction_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='lnmtransaction',
            name='confirmation_request',
            field=models.TextField(max_length=3000, null=True),
        ),
        migrations.AddField(
            model_name='lnmtransaction',
            name='validation_request',
            field=models.TextField(max_length=3000, null=True),
        ),
    ]
