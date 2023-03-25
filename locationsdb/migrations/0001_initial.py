# Generated by Django 4.1.7 on 2023-03-23 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.TextField(max_length=200, verbose_name='Location name')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('location_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='locationsdb.location')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('locationsdb.location',),
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('location_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='locationsdb.location')),
                ('building_int', models.IntegerField(default=0, verbose_name='Building number')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('locationsdb.location',),
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('location_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='locationsdb.location')),
                ('area_ref', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='locationsdb.area')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('locationsdb.location',),
        ),
        migrations.CreateModel(
            name='Installation',
            fields=[
                ('building_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='locationsdb.building')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('locationsdb.building',),
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('building_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='locationsdb.building')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('locationsdb.building',),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('zone_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='locationsdb.zone')),
                ('room_number', models.IntegerField(verbose_name='Level')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('locationsdb.zone',),
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('zone_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='locationsdb.zone')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('locationsdb.zone',),
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('location_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='locationsdb.location')),
                ('level_int', models.IntegerField(verbose_name='Level')),
                ('building_ref', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='locationsdb.building')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('locationsdb.location',),
        ),
        migrations.AddField(
            model_name='area',
            name='level_ref',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='locationsdb.level'),
        ),
    ]
