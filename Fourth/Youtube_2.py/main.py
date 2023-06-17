import json
import typing as tp

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from datetime import datetime
from matplotlib.figure import Figure


class YouTube2:
    def __init__(
            self,
            trends_df_path: str = "RUvideos_short.csv",
            categories_df_path: str = "RU_category_id.json"
    ):
        self.trends_df = pd.read_csv('RUvideos_short.csv')
        self.trends_df['trending_date'] = pd.to_datetime(self.trends_df['trending_date'], format='%y.%d.%m')

        with open(categories_df_path) as json_file:
            json_data = json.load(json_file)

        self.categories_df = pd.DataFrame(columns=['id', 'name'])

        for item in json_data['items']:
            self.categories_df = self.categories_df.append(
                {'id': int(item['id']),
                 'name': item['snippet']['title']},
                ignore_index=True
            )

        self.categories_df['id'] = self.categories_df['id'].astype(int)

    def task1(self) -> pd.DataFrame:
        self.trends_df = self.trends_df.merge(self.categories_df, left_on='category_id', right_on='id')
        return self.trends_df

    def task2(self) -> pd.DataFrame:
        return pd.pivot_table(self.trends_df, values='views', index='name', columns='trending_date', aggfunc='sum')

    def task3(self) -> Figure:
        df = pd.pivot_table(self.trends_df, values='views', index='name', columns='trending_date', aggfunc='sum')
        sns.heatmap(df / 1000000, annot=True, vmin=-5, vmax=5, center=0, linewidths=1, linecolor='black', cbar=False)
        plt.suptitle("Category views on the heatmap for the date")
        return plt.gcf()

    def task4(self) -> pd.DataFrame:
        self.trends_df = pd.pivot_table(self.trends_df, values='views', index='name', columns='trending_date',
                                        aggfunc='sum', margins=True, margins_name='Всего просмотров')
        return self.trends_df

    def task5(self) -> Figure:
        sns.heatmap(self.trends_df / 1000000, annot=True, vmin=-5, vmax=5)
        plt.suptitle("Category views on the heatmap for the date")
        plt.gca().set_xlabel('Дата')
        plt.gca().set_ylabel('Категория')
        return plt.gcf()
