from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from core.models import MainSector, SubSector, Skills
admin.site.register(MainSector)
admin.site.register(SubSector)
admin.site.register(Skills)

# @admin.register(Skills)
# class SkillsAdmin(ImportExportModelAdmin):
#     model = Skills
#
#     save_as = True
#
#
# @admin.register(MainSector)
# class MainSectorAdmin(ImportExportModelAdmin):
#     model = MainSector
#
#     save_as = True
#
#
# @admin.register(SubSector)
# class SubSectorAdmin(ImportExportModelAdmin):
#     model = SubSector
#
#     save_as = True
