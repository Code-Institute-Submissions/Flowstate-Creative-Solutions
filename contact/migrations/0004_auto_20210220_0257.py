# Generated by Django 3.1.5 on 2021-02-20 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_contact_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='user',
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_motive',
            field=models.CharField(choices=[('general_enquiry', 'General Enquiry'), ('product_technical_assistance', 'Product Technical Assistance'), ('product_suggestion', 'Product Suggestion'), ('general_feedback', 'General Feedback')], default='general_enquiry', max_length=120),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
