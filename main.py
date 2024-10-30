from operator import itemgetter


class Faculty:
    """Факультет"""

    def __init__(self, id, name, num_employees):
        self.id = id
        self.name = name
        self.num_employees = num_employees


class University:
    """Университет"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class FacultyUniversity:
    """
    'Факультеты университета' для реализации
    связи многие ко-многИМ
    """

    def __init__(self, university_id, faculty_id):
        self.university_id = university_id
        self.faculty_id = faculty_id


# Факультеты
faculties = [
    Faculty(1, 'Факультет информационных технологий', 150),
    Faculty(2, 'Факультет экономики', 120),
    Faculty(3, 'Факультет гуманитарных наук', 80),
    Faculty(4, 'Факультет права', 100),
]

# Университеты
universities = [
    University(1, 'Московский государственный университет'),
    University(2, 'Санкт-Петербургский государственный университет'),
    University(3, 'Казанский федеральный университет'),
    University(4, 'Сибирский федеральный университет'),
    University(5, 'МГТУ им. Баумана'),
]

# Деканы (список)
decans = [
    ('Иванов', 1),
    ('Петров', 2),
    ('Сидоров', 3),
    ('Кузнецов', 4),
    ('Смирнов', 1),  # Добавили декана с фамилией, заканчивающейся на "ов"
]

faculties_universities = [
    FacultyUniversity(1, 1),
    FacultyUniversity(2, 2),
    FacultyUniversity(1, 3),
    FacultyUniversity(2, 4),
    FacultyUniversity(3, 1),
    FacultyUniversity(4, 2),
    FacultyUniversity(3, 4),
    FacultyUniversity(5, 1),
    FacultyUniversity(5, 2),
]


def main():
    """Основная функция"""
    # Соединение данных один-ко-многим
    one_to_many = [(f.name, u.name)
                   for u in universities
                   for f in faculties
                   if f.id == u.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(u.name, fu.university_id, fu.faculty_id)
                         for u in universities
                         for fu in faculties_universities
                         if u.id == fu.university_id]
    many_to_many = [(f.name, u_name)
                    for u_name, university_id, faculty_id in many_to_many_temp
                    for f in faculties if f.id == faculty_id]

    print('Задание Б1')
    res_11 = sorted(one_to_many, key=itemgetter(0))
    print(res_11)

    print('\nЗадание Б2')
    res_12_unsorted = []
    for u in universities:
        u_faculties = list(filter(lambda i: i[1] == u.name, one_to_many))
        if len(u_faculties) > 0:
            total_employees = sum(f.num_employees for f in faculties if f.name in [x[0] for x in u_faculties])
            res_12_unsorted.append((u.name, total_employees))
    res_12 = sorted(res_12_unsorted, key=itemgetter(1))
    print(res_12)

    print('\nЗадание Б3')
    res_13_new = []
    for d in decans:
        if d[0].endswith('ов'):
            for f_name, u_name, faculty_id in many_to_many_temp:
                if d[1] == faculty_id:
                    res_13_new.append((d[0], u_name))
                    break
    print(res_13_new)


if __name__ == '__main__':
    main()
