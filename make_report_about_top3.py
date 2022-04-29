import pandas as pd


def make_report_about_top3(students_avg_scores):
    df = pd.DataFrame(list(zip(students_avg_scores.keys(), students_avg_scores.values())),
                      columns=['names', 'avg_score'])
    df = df.sort_values('avg_score', ascending=False).head(3)
    df.to_excel('./avg_scores.xlsx')
