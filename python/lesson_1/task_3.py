print('Welcome to medical card')

name = input('Please input name: ')
surname = input('Please input surname: ')
age = int(input('Please input age: '))
weight = int(input('Please input weight: '))

medical_info = name + ' ' + surname + ', ' + str(age) + ' years,' + ' weight ' + str(weight)

good_condition = 'good condition'
must_take_care = 'should take yourself'
need_a_doctor = 'need a doctor!'


if weight >= 50 and weight <= 120:
    if age < 30:
        print(medical_info + ' - ' + good_condition)
    elif age >= 40:
        print(medical_info + ' - ' + good_condition) #not in task
    else:
        print(medical_info + ' - ' + good_condition) #not in task
else:
    if age < 30:
        print(medical_info + ' - ' + must_take_care) #not in task
    elif age >= 40:
        print(medical_info + ' - ' + need_a_doctor)
    else:
        print(medical_info + ' - ' + must_take_care)
