# Generated by Django 2.0.4 on 2018-04-10 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bin_packages', '0001_initial'),
        ('src_packages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Hostname.', max_length=255, unique=True)),
                ('running_kernel', models.CharField(help_text='Running kernel version.', max_length=255, default='')),
                ('running_kernel_slug', models.SlugField(
                    help_text='Running kernel version URL slug.', max_length=255, default='')),
                ('created', models.DateTimeField(
                    auto_now_add=True, help_text='Datetime of the creation of this object.')),
                ('modified', models.DateTimeField(
                    auto_now=True, help_text='Datetime of the last modification of this object.')),
                ('os', models.ForeignKey(
                    help_text='Operating system.', on_delete=django.db.models.deletion.PROTECT, related_name='+',
                    to='src_packages.OS', verbose_name='operating system')),
            ],
            options={
                'verbose_name': 'host',
                'verbose_name_plural': 'hosts',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='HostPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upgrade_type', models.CharField(
                    blank=True, help_text='Upgrade type (security)', max_length=255, null=True)),
                ('created', models.DateTimeField(
                    auto_now_add=True, help_text='Datetime of the creation of this object.')),
                ('modified', models.DateTimeField(
                    auto_now=True, help_text='Datetime of the last modification of this object.')),
                ('host', models.ForeignKey(
                    help_text='Host.', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='hosts.Host')),
                ('package', models.ForeignKey(
                    help_text='Binary package.', on_delete=django.db.models.deletion.PROTECT,
                    related_name='installed_hosts', to='bin_packages.Package', verbose_name='binary package')),
                ('package_version', models.ForeignKey(
                    help_text='Binary package version.', on_delete=django.db.models.deletion.PROTECT,
                    related_name='installed_hosts', to='bin_packages.PackageVersion',
                    verbose_name='binary package version')),
                ('upgradable_package', models.ForeignKey(
                    blank=True, help_text='Upgradable binary package.', null=True,
                    on_delete=django.db.models.deletion.PROTECT, related_name='upgradable_hosts',
                    to='bin_packages.Package', verbose_name='upgradable binary package')),
                ('upgradable_version', models.ForeignKey(
                    blank=True, help_text='Upgradable binary package version.', null=True,
                    on_delete=django.db.models.deletion.PROTECT, related_name='upgradable_hosts',
                    to='bin_packages.PackageVersion', verbose_name='upgradable binary package version')),
            ],
            options={
                'verbose_name': 'host package',
                'verbose_name_plural': 'host packages',
                'ordering': ['host__name', 'package__name', 'package_version__version'],
            },
        ),
        migrations.AddField(
            model_name='host',
            name='package_versions',
            field=models.ManyToManyField(
                blank=True, db_index=True, help_text='Binary package versions installed on this host.',
                related_name='_host_package_versions_+', through='hosts.HostPackage', to='bin_packages.PackageVersion',
                verbose_name='binary package versions'),
        ),
        migrations.AddField(
            model_name='host',
            name='packages',
            field=models.ManyToManyField(
                blank=True, db_index=True, help_text='Binary packages installed on this host.',
                related_name='_host_packages_+', through='hosts.HostPackage', to='bin_packages.Package',
                verbose_name='binary packages'),
        ),
        migrations.AddField(
            model_name='host',
            name='upgradable_packages',
            field=models.ManyToManyField(
                blank=True, db_index=True, help_text='Binary packages installed on this host that could be upgraded.',
                related_name='_host_upgradable_packages_+', through='hosts.HostPackage', to='bin_packages.Package',
                verbose_name='upgradable binary packages'),
        ),
        migrations.AddField(
            model_name='host',
            name='upgradable_versions',
            field=models.ManyToManyField(
                blank=True, db_index=True,
                help_text='Binary package versions installed on this host that could be upgraded.',
                related_name='_host_upgradable_versions_+', through='hosts.HostPackage',
                to='bin_packages.PackageVersion', verbose_name='upgradable binary package versions'),
        ),
        migrations.AlterUniqueTogether(
            name='hostpackage',
            unique_together={('host', 'package')},
        ),
    ]
