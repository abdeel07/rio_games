# Generated by Django 4.0.4 on 2022-06-03 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Rio', '0005_quiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quiz', to='Rio.category'),
        ),
    ]