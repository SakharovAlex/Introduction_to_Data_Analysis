import pandas as pd
import matplotlib.pyplot as plt
import typing as tp
from matplotlib.axes import Axes


class CatExam:
    def __init__(self, path_to_df: str = "cat_exam_data.csv"):
        self.df = pd.read_csv('cat_exam_data.csv')

    def task1(self) -> pd.DataFrame:
        return self.df.head(5)

    def task2(self) -> tp.List[str]:
        table = self.df.isna().mean()
        return list(table[table > 0].index)

    def task3(self) -> pd.DataFrame:
        return self.df.dropna()

    def task4(self) -> pd.DataFrame:
        return self.df.dropna().describe()

    def task5(self) -> int:
        return (self.df[self.df.test_score == 100.0]).shape[0]

    def task6(self) -> pd.DataFrame:
        grouped_df = self.df.dropna()[self.df.dropna().test_score == 100.0].groupby('school').count()
        sorted_df = grouped_df.sort_values(['number_of_students', 'school'], ascending=False).reset_index()
        merged_df = sorted_df.merge(self.df.dropna().drop('test_score', axis=1), on='school').drop_duplicates()
        dropped_df = merged_df.drop('number_of_students_x', axis=1)
        renamed_df = dropped_df.rename(columns={'number_of_students_y': 'number_of_students'})
        df = renamed_df[['school', 'number_of_students', 'test_score']].reset_index().drop('index', axis=1)
        return df.rename(columns={'test_score': 'cnt_100'})

    def task7(self) -> pd.DataFrame:
        return self.df.groupby('school').agg('mean').sort_values('test_score', ascending=False).head(10).reset_index()

    def task8(self) -> pd.DataFrame:
        return self.df.groupby('school').agg('mean').sort_values('test_score', ascending=False).tail(10).reset_index()

    def task9(self) -> Axes:
        small_school_df = self.df.dropna()[self.df.dropna().number_of_students <= 1000].drop('school', axis=1)
        big_school_df = self.df.dropna()[self.df.dropna().number_of_students > 1000].drop('school', axis=1)
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        plt.title('UCE results in big and small schools')
        plt.xlabel('Test results')
        plt.ylabel('Number of students')
        plt.hist(big_school_df['test_score'], label="1 type(big)", bins=10, alpha=0.5, color="g")
        plt.hist(small_school_df['test_score'], label="2 type(small)", bins=10, alpha=0.5, color="b")
        plt.legend()
        return plt.gca()
