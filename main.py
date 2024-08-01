import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

#SaintEkler on twitter

app = dash.Dash(__name__)


data_path = 'data.csv' 
df = pd.read_csv(data_path)


print(df.columns)


df = df.sort_values(by='Years_of_Experience')


fig = px.line(
    df,
    x='Years_of_Experience',
    y='Salary',
    line_shape='linear',
    title='Salary vs Work experience',
    labels={'Years_of_Experience': 'Work experience (years)', 'Salary': 'Salary ($)'}
)


fig.update_traces(
    mode='lines+markers',
    marker=dict(size=10)
)


app.layout = html.Div(
    children=[
        html.H1(children="Analyzing employee data"),
        dcc.Graph(
            id='salary-vs-experience',
            figure=fig
        ),
        dcc.Graph(
            id='age-vs-salary',
            figure=px.histogram(
                df,
                nbins=10,
                color_discrete_sequence=['indianred'],
                x='Age',
                y='Salary',
                title='Salary by age',
                labels={'Age': 'Age', 'Salary': 'Salary ($)'}
            )
        ),
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)
