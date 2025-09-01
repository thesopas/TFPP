from academy_management import AcademyManagement as AM
academia = AM()
programacion_1 = academia.create_course(name='Programación 1', code='P1')

print(programacion_1.name)
print(programacion_1.code)
