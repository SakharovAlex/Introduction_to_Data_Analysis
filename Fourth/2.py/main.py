from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.figure import Figure
import typing as tp

class YouTube:
    def __init__(self, path_to_df: str = "RUvideos_short.csv"):
        self.df = pd.read_csv('RUvideos_short.csv')

    def task1(self) -> pd.DataFrame:
        self.df['trending_date'] = pd.to_datetime(self.df['trending_date'], format = '%y.%d.%m')
        return self.df

    def task2(self) -> pd.DataFrame:
        self.df = self.df[['trending_date', 'category_id', 'views', 'likes', 'dislikes', 'comment_count']]
        self.df['trending_date'] = self.df['trending_date'].dt.day
        return self.df

    def task3(self) -> Figure:
        with sns.plotting_context(font_scale = 1), sns.axes_style("whitegrid"):
            plt.figure(figsize = (8, 8))
            sns.boxplot(data = self.df, x = 'trending_date', y = 'views').set_title('View statistics')
        return plt.gcf()

    def task4(self) -> Figure:
        with sns.plotting_context(font_scale = 1), sns.axes_style("whitegrid"):
            plt.figure(figsize = (8, 8))
            sns.boxplot(data = self.df, x = 'trending_date', y = 'views').set_title('View statistics')
            plt.ylim((0, 600000))
        return plt.gcf()

    def task5(self) -> Figure:
        with sns.plotting_context("notebook", font_scale = 1), sns.axes_style("whitegrid"):
            sns.jointplot(x = 'views', y = 'likes', data = self.df, kind = 'scatter', color = "b", alpha = 0.5)
            plt.suptitle("Like and view jointplot")
        return plt.gcf()

    def task6(self) -> Figure:
        df = self.df[(self.df['views'] > self.df['views'].quantile(0.1)) & (self.df['views'] < self.df['views'].quantile(0.75))]
        with sns.plotting_context("notebook", font_scale = 1), sns.axes_style("whitegrid"):
            sns.jointplot(x = 'views', y = 'likes', data = df, kind = 'scatter', color = "b", alpha = 0.5)
            plt.suptitle("Like and view jointplot")
        return plt.gcf()

