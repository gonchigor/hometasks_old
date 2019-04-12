# Generated by Django 2.2 on 2019-04-08 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dimensionsapp', '0005_author_biography'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название книги')),
                ('image_field', models.ImageField(upload_to='', verbose_name='Фото обложки')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Цена (BYN)')),
                ('year_publishing', models.PositiveIntegerField(verbose_name='Год издания')),
                ('count_pages', models.PositiveIntegerField(verbose_name='Количество страниц')),
                ('isbn', models.CharField(max_length=13, verbose_name='ISBN')),
                ('weight', models.FloatField(verbose_name='Вес (гр)')),
                ('age_restrictions', models.CharField(max_length=50, verbose_name='Возрастные ограничения')),
                ('count_books', models.PositiveIntegerField(verbose_name='Количество книг в наличии')),
                ('is_active', models.BooleanField(verbose_name='Активный (доступен для заказа)')),
                ('rate', models.FloatField(verbose_name='Рейтинг')),
                ('date_create', models.DateField(auto_now_add=True, verbose_name='Дата внесения в каталог')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения карточки')),
                ('authors', models.ManyToManyField(to='dimensionsapp.Author')),
                ('binding', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dimensionsapp.Binding')),
                ('format_book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dimensionsapp.FormatBook')),
                ('jenre', models.ManyToManyField(to='dimensionsapp.Jenre')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dimensionsapp.PublishingHouse')),
                ('serie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dimensionsapp.Serie')),
            ],
        ),
    ]