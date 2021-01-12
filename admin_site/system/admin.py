
from django.contrib import admin

from .models import Configuration, ConfigurationEntry, PackageList, Package
from .models import Site, Distribution, PCGroup, PC, CustomPackages
from .models import PackageInstallInfo, PackageStatus, ImageVersion
from .models import SecurityEvent, SecurityProblem
# Job-related stuff
from .models import Script, Batch, Job, Input, BatchParameter
from .models import AssociatedScript, AssociatedScriptParameter
ar = admin.site.register


class PackageInstallInfoInline(admin.TabularInline):
    model = PackageInstallInfo
    extra = 3


class PackageStatusInline(admin.TabularInline):
    model = PackageStatus
    extra = 3


class ConfigurationEntryInline(admin.TabularInline):
    model = ConfigurationEntry
    extra = 3


class PackageListAdmin(admin.ModelAdmin):
    inlines = [PackageStatusInline]


class CustomPackagesAdmin(admin.ModelAdmin):
    inlines = [PackageInstallInfoInline]


class ConfigurationAdmin(admin.ModelAdmin):
    fields = ['name']
    inlines = [ConfigurationEntryInline]


class PCInline(admin.TabularInline):
    model = PC.pc_groups.through
    extra = 3


class PCGroupAdmin(admin.ModelAdmin):
    inlines = [PCInline]


class JobInline(admin.TabularInline):
    fields = ['pc']
    model = Job
    extra = 1


class BatchParameterInline(admin.TabularInline):
    model = BatchParameter
    extra = 1


class BatchAdmin(admin.ModelAdmin):
    fields = ['site', 'name', 'script']
    inlines = [JobInline, BatchParameterInline]


class AssociatedScriptParameterInline(admin.TabularInline):
    model = AssociatedScriptParameter
    extra = 1


class InputInline(admin.TabularInline):
    model = Input
    extra = 1


class ScriptAdmin(admin.ModelAdmin):
    inlines = [InputInline]


ar(Configuration, ConfigurationAdmin)
ar(PackageList)
ar(CustomPackages, CustomPackagesAdmin)
ar(Site)
ar(Distribution)
ar(PCGroup, PCGroupAdmin)
ar(PC)
ar(Package)
ar(ImageVersion)
# Job related stuff
ar(Script, ScriptAdmin)
ar(Batch, BatchAdmin)
ar(Job)
ar(BatchParameter)
ar(AssociatedScript)
ar(AssociatedScriptParameter)
ar(SecurityEvent)
ar(SecurityProblem)
