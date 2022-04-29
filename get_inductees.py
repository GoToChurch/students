import pandas as pd
from datetime import datetime


def get_inductees(names, birthday_years, genders):
    df = pd.DataFrame(list(zip(names, birthday_years, genders)),
                      columns =['names', 'birthday_years', 'genders'])
    current_year = datetime.now().year
    df['age'] = current_year - df.birthday_years
    inductees = df.query('age >= 18 & age <= 30 & genders == "Male"')
    anons = df.query('age.isna() | genders.isna()')
    return list(inductees.names), list(anons.names)

print(get_inductees(names, birthday_years, genders))
