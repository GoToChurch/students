import pandas as pd


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
