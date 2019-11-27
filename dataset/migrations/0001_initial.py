# Generated by Django 2.2.7 on 2019-11-27 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worker_id', models.CharField(max_length=30)),
                ('age_group', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=30)),
                ('ethnicity', models.CharField(max_length=30)),
                ('education', models.CharField(max_length=30)),
                ('marital', models.CharField(max_length=30)),
                ('income', models.CharField(max_length=30)),
                ('employment', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=30)),
                ('task_name', models.CharField(max_length=30)),
                ('workers', models.ManyToManyField(through='dataset.Result', to='dataset.Worker')),
            ],
        ),
        migrations.AddField(
            model_name='result',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataset.Task'),
        ),
        migrations.AddField(
            model_name='result',
            name='worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataset.Worker'),
        ),
    ]
