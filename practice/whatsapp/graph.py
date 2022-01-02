import matplotlib.pyplot as plt
import pandas as pd
from . import readwhatsappchat as wa
import numpy as np
import os

def File(file):
    df = wa.Algo(file)
    df['date'] = pd.to_datetime(df['date'], format='%m/%d/%y')
    return df

def Overall(df, location):
    df = File(df)
    overall = df.loc[df.message != 'NaN'].groupby('date').size().rename('counts'); overall = overall.to_frame().reset_index()
    overall_nan = df.loc[df.message == 'NaN'].groupby('date').size().rename('counts'); overall_nan = overall_nan.to_frame().reset_index()
    overall_nan.counts.loc[overall_nan.counts != 0] = 0
    overall = pd.concat([overall, overall_nan]).groupby('date').sum()

    plt.figure(figsize=(25,10))
    plt.plot(overall)
    plt.yticks(range(0, overall['counts'].max()+5, 5))
    plt.savefig(os.path.join(location, 'overall.jpg'))