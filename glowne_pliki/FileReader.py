import pandas as pd


class FileReader:
    def __init__(self, filepath):
        self.__df = pd.read_csv(filepath, na_values=(":", "NaN"))
        self.__header = list(self.__df.columns)
        # Utworzenie listy poszczegolnych tytulow dat
        self.__dates = list(self.__df.columns[1:])
        # Utworzenie czystej listy panstw
        self.__countries = list(self.__df[self.__header[0]])
        self.__countries = self.__countries[3:]
        # Skrocenie nazw panstw
        for a in range(0, len(self.__countries)):
            self.__check_for_length_of_countries = self.__countries[a].split(" ")
            if len(self.__check_for_length_of_countries) >= 2 and self.__check_for_length_of_countries[1][0] == "(":
                self.__countries[a] = self.__check_for_length_of_countries[0]

    def __repr__(self):
        class_name = self.__class__.__name__
        attrs = {k.split("__")[-1]: v for k, v in self.__dict__.items()}
        return f"({class_name}): {attrs}"

    def getData(self):
        return self.__df

    def getDates(self):
        return self.__dates

    def getCountries(self):
        return self.__countries


class Country:
    def __init__(self, name_of_country, data):
        self.__date = None
        self.__name_of_country = name_of_country
        self.__data = data.getData()
        self.__list_of_countries = data.getCountries()
        self.__list_of_dates = data.getDates()

    def get_country_value_from_date(self, date):
        self.__date = date
        return self.__data.iloc[self.__list_of_countries.index(self.__name_of_country) + 3, self.__list_of_dates.index(
            self.__date) + 1]


if __name__ == "__main__":
    test = FileReader("eurostat.csv")
    poland = Country("Poland", test)
    poland.get_country_value_from_date("2019-S1")
