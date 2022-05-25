import pandas as pd


class FileReader:
    def __init__(self, filepath):
        # Wczytanie pliku wraz z zamiana ":" - (pustych miejsc) na "NaN"
        self.__df = pd.read_csv(filepath, na_values=(":", "NaN"))
        # Utworzenie listy poszczegolnych tytulow dat
        self.__dates = list(self.__df.columns[1:])
        # Utworzenie listy panstw
        self.__countries = self.__create_clear_list_of_countries()

    # Funkcja tworzaca czysta, mozliwa do latwego uzycia liste panstw
    def __create_clear_list_of_countries(self):
        header = list(self.__df.columns)
        countries = list(self.__df[header[0]])
        countries = countries[3:]
        countries = self.__shorten_countries_names(countries)
        return countries

    # Funkcja sluzaca do usuwania dlugich nawiasow z nazw panstw
    def __shorten_countries_names(self, list_of_countries):
        for a in range(0, len(list_of_countries)):
            check_for_length_of_countries = list_of_countries[a].split(" ")
            if len(check_for_length_of_countries) >= 2 and check_for_length_of_countries[1][0] == "(":
                list_of_countries[a] = check_for_length_of_countries[0]
        return list_of_countries

    def __repr__(self):
        class_name = self.__class__.__name__
        attrs = {k.split("__")[-1]: v for k, v in self.__dict__.items()}
        return f"({class_name}): {attrs}"

    def get_data(self):
        return self.__df

    def get_dates(self):
        return self.__dates

    def get_countries(self):
        return self.__countries


class Country:
    def __init__(self, name_of_country, data):
        self.__name_of_country = name_of_country
        self.__data = data.get_data()
        self.__list_of_countries = data.get_countries()
        self.__list_of_dates = data.get_dates()


    # Funkcja zwracająca listę wszystkich wartosci dla danego panstwa
    def get_all_values_for_country(self):
        country_num = self.__give_country_num()
        values_for_country = list(self.__data.iloc[country_num])
        values_for_country = values_for_country[1:]
        return values_for_country

    # Funkcja zwracajaca wartosci dla danego panstwa i danego okresu
    def get_country_value_from_date(self, date):
        country_num = self.__give_country_num()
        date_num = self.__give_date_num(date)
        value_on_date = self.__data.iloc[country_num, date_num]
        return value_on_date

    # Funkcja zwracajaca odpowiedni numer wiersza po kraju
    def __give_country_num(self):
        country_num = self.__list_of_countries.index(self.__name_of_country) + 3
        return country_num

    # Funkcja zwracajaca odpowiedni numer kolumny po dacie
    def __give_date_num(self, date):
        date_num = self.__list_of_dates.index(date) + 1
        return date_num


if __name__ == "__main__":
    test = FileReader("eurostat.csv")
    poland = Country("Poland", test)
    poland.get_country_value_from_date("2009-S1")
    print(poland.get_all_values_for_country())

    print(test.get_dates()[4])
    for a in range(0, len(test.get_countries())):
        country = Country(test.get_countries()[a], test)
        date = country.get_country_value_from_date(test.get_dates()[4])
        print((test.get_countries()[a], date))

