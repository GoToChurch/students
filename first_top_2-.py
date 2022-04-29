import pandas as pd


candidates = [
 {"name": "Vasya",  "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores":0},
 {"name": "Fedya",  "scores": {"math": 33, "russian_language": 85, "computer_science": 42},  "extra_scores":2},
 {"name": "Petya",  "scores": {"math": 92, "russian_language": 33, "computer_science": 34},  "extra_scores":1}
]

def first_top_20(candidates):
    for i in candidates:
        i['math'] = i.get('scores').get('math')
        i['russian_language'] = i.get('scores').get('russian_language')
        i['computer_science'] = i.get('scores').get('computer_science')
    candidates_df = pd.DataFrame(candidates).drop('scores', axis=1)
    candidates_df['sum_scores'] = candidates_df.values[:, 1:].sum(1)
    candidates_df = candidates_df.sort_values(['sum_scores', 'computer_science', 'math'], ascending=False)
    return list(candidates_df.name.head(20))

print(first_top_20(candidates))
