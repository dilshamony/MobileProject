# Generated by Django 3.2 on 2021-05-10 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0002_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveBigIntegerField(default=1)),
                ('price_total', models.PositiveBigIntegerField(blank=True, editable=False, null=True)),
                ('user', models.CharField(max_length=120, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobile.product')),
            ],
        ),
    ]
