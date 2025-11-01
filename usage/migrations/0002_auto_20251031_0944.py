from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('usage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='materialusage',
            name='issued_to',
            field=models.CharField(max_length=100, default=''),
        ),
    ]
