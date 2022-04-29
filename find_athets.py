def find_athelets(know_english, sportsmen, more_than_20_years):
    athlets = list(set(know_english) & set(sportsmen) & set(more_than_20_years))
    return  athlets

print(find_athelets(know_english, sportsmen, more_than_20_years))
