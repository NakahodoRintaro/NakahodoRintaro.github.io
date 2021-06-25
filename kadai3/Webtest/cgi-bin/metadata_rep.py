# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

def generate_df_html(df):
    target = '<table border="1">\n'
    for row in np.array(df):
        target += '<tr>\n'
        for elem in row:
            target += f'<td>{elem}</td>\n'
        target += '</tr>\n'
    target += '</table>'
    return target