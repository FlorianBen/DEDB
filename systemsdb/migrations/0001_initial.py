# Generated by Django 4.1.7 on 2023-03-23 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.TextField(max_length=200, verbose_name='Name')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='GroupSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.TextField(max_length=200, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('basesystem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='systemsdb.basesystem')),
                ('group_ref', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='systemsdb.groupsystem')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('systemsdb.basesystem',),
        ),
        migrations.CreateModel(
            name='SubSystem',
            fields=[
                ('basesystem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='systemsdb.basesystem')),
                ('system_ref', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='systemsdb.system')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('systemsdb.basesystem',),
        ),
    ]
