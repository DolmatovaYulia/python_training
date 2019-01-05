from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact
# from pymysql.converters import encoders, decoders, convert_mysql_timestamp


class ORMFixture:
    # Объект, на основании которого построена привязка
    db = Database()

    # Привязка в виде набора классов
    # Класс описывает объекты, которые будут сохраняться в эту БД
    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixture.ORMContact, table='address_in_groups', column='id', reverse='groups', lazy=True)

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup, table='address_in_groups', column='group_id', reverse='contacts', lazy=True)

    def __init__(self, host, name, user, password):
        # conv = encoders
        # conv.update(decoders)
        # conv[datetime] = convert_mysql_timestamp
        # Привязка к БД при помощи метода bind
        self.db.bind('mysql', host=host, database=name, user=user, password=password)  # conv=conv
        # Сопоставление свойств описанных классов с таблицами и полями таблиц (__table__)
        self.db.generate_mapping()
        sql_debug(True)

    # Преобразование из объектов типа ORMGroup в модельные объекты
    def convert_groups_to_model(self, groups):
        # Функция, конфертирующая отдельно взятую группу
        def convert(group):
            return Group(id=str(group.id), group_name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    def convert_contacts_to_model(self, contacts):
        # Функция, конфертирующая отдельно взятую группу
        def convert(contact):
            return Contact(id=str(contact.id), firstname=contact.firstname, lastname=contact.lastname)
        return list(map(convert, contacts))

    # Функции, которые получают списки объектов
    # Выполняются в рамках сессии
    @db_session
    def get_group_list(self):
        # Делаем выборку из объектов класса
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_contact_list(self):
        # Делаем выборку из объектов класса
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    # Метод, получающий список контактов, которые входят в какую-либо группу
    @db_session
    def get_contacts_in_group(self, group):
        # Получаем объект типа ORMGroup, который соответствует переданному модельному объекту
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        # Преобразуем объекты типа ORMContact в модельные объекты
        return self.convert_contacts_to_model(orm_group.contacts)

    # Метод, получающий список контактов, которые не входят в какую-либо группу
    @db_session
    def get_contacts_not_in_group(self, group):
        # Получаем объект типа ORMGroup, который соответствует переданному модельному объекту
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        # Выбираем все контакты, у которых список групп не содержит заданную группу
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups))

    @db_session
    def get_groups_with_contacts(self):
        all_groups = self.get_group_list()
        return list(g for g in all_groups if len(self.get_contacts_in_group(g)) > 0)
