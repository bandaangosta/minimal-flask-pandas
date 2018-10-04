from flask import render_template
import pandas as pd

from minimalflaskpandas import app


@app.route('/')
def index():
    df = pd.DataFrame({ 'A' : 1.,
                        'B' : pd.Timestamp('20130102'),
                        'C' : pd.Series(1,index=list(range(4)), dtype='float32'),
                        'D' : pd.Categorical(["test", "train", "test", "train"]),
                        'E' : 'foo' })

    return render_template('index.html', data=df.itertuples())
