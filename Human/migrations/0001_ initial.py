from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = [
    ]
    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_surname', models.CharField(max_length=150)),
                ('biografia', models.TextField(blank=True)),
                ('birthdate', models.DateTimeField(help_text='birthdate')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('photo', models.ImageField(upload_to='media/%Y/%m/%d')),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]
