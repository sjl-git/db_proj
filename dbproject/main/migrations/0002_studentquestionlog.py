# Generated by Django 2.1.7 on 2019-12-01 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentQuestionLog',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('score', models.IntegerField()),
                ('question_field', models.ForeignKey(db_column='question_id', on_delete=django.db.models.deletion.CASCADE, to='main.Questions')),
                ('user_field', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='main.Users')),
            ],
            options={
                'db_table': 'Student_Question_Log',
                'managed': True,
            },
        ),
    ]