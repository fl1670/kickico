import datetime
import time

now = datetime.datetime.now()


class work_with_time:

    # Возвращяет строку "08.09.2017 10:59"
    def get_time_now(self):
        return now.strftime("%d.%m.%Y %H:%M")

    # Возвращяет строку "080920171059"
    def get_time_now_2(self):
        return now.strftime("%d%m%Y%H%M")

    # Возвращяет строку "2017.08.09 10:59:59"
    def get_date_time_Y_m_d_H_M_S(self):
        return time.strftime("%Y.%m.%d %H:%M:%S")

    # Возвращяет (текущую дату + timedelta_days) ввиде строки "08.09.2017"
    def date_increased_x_days(self, timedelta_days):
        datetime2 = now + datetime.timedelta(days=timedelta_days)
        return datetime2.strftime("%d.%m.%Y")

    # Возвращяет (текущую дату + timedelta_days) ввиде строки "08.09.2017"
    def date_add_x_dayTime(self, date, timedelta_days, timedelta_hours):
        datetime2 = date + datetime.timedelta(days=timedelta_days, hours=timedelta_hours)
        return datetime2

    # Возвращает текущую дату
    def get_date_now(self):
        return now.strftime("%d.%m.%Y")

    # Входная строка должна быть "08.09.2017 10:00:00"
    def convert_string_to_date(self, string):
        return datetime.datetime.strptime(string, "%d.%m.%Y %H:%M:%S")

    # Выходная дата будет в виде "08.09.2017 10:00:00"
    def convert_date_to_string(self, date):
        return datetime.datetime.strftime(date, "%d.%m.%Y %H:%M:%S")

    # Возвращяет дату "2015-07-25 00:00:00.000"
    def get_date_time_for_sql(self):
        date_text = time.strftime("%Y-%m-%d %H:%M:%S")
        date_text = date_text + '.000'
        return date_text

    # Возвращяет дату "2015-07-25 00:00:00.000"
    def get_date_time_for_sql_increased_x_days(self, timedelta_days):
        datetime2 = now + datetime.timedelta(days=timedelta_days)
        temp = datetime2.strftime("%Y-%m-%d %H:%M:%S")
        temp = temp + '.000'
        return temp

    # Возвращяет (текущую дату + timedelta_days) ввиде строки "2018-10-23T11:15:55+03:00"
    def get_date_increased_x_days_json(self, timedelta_days):
        datetime2 = now + datetime.timedelta(days=timedelta_days)
        return datetime2.strftime("%Y-%m-%dT%H:%M:%S+03:00")

    # Конвертация запрещенных (для использования в URL) символов в разрешенные
    def date_cast_to_date_for_URL(self, Date):
        Date = Date[:Date.find("+03:00")]
        Date = Date.replace("+", "%2B")
        new_Date = Date.replace(":", "%3A")
        return new_Date

    def convert_date(self, date):
        new_date = datetime.datetime.strptime(date, '%d.%m.%Y')
        return new_date.strftime("%Y-%m-%dT%H:%M:%S+03:00")

    def convert_date_time(self, date):
        new_date = datetime.datetime.strptime(date, '%d.%m.%Y %H:%M')
        return new_date.strftime("%Y-%m-%dT%H:%M:%S+03:00")

    # Возвращяет текущую дату ввиде строки 20191001175409
    def get_date_time_Users_API(self):
        return time.strftime("%Y%m%d%H%M%S")

