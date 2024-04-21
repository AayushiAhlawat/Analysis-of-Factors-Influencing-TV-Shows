# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html, callback, dash_table, Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.LUX])


# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df_twitter = pd.read_csv("shows_polarity.csv")
df_twitter['show_name'] = df_twitter['show_name'].str.replace('_',' ')
df_twitter['show_name'] = df_twitter['show_name'].str.replace('df',' ')

fig_twitter = px.bar(df_twitter, x="show_name", y=["positive", "negative"], barmode="group")

df = pd.read_csv('class.csv')
df.columns = ['subreddit', 'no_of_post_by_subreddit']
df = df.drop(labels=0, axis=0)
df2 = pd.read_csv('date_com.csv')
df2.columns = ['date', 'no_of_comments']

fig = px.bar(df, x="subreddit", y="no_of_post_by_subreddit",)

fig1 = go.Figure(data=go.Scatter(x=df2['date'].astype(dtype=str), 
                                y=df2['no_of_comments'],
                                marker_color='black', text="counts"))
fig1.update_layout({
                   "xaxis": {"title":"Time"},
                   "yaxis": {"title":"Total comments"},
                   "showlegend": False})


def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

df_tmdb = pd.read_csv('predictions.csv')

app.layout = html.Div( children= [html.H1(children = ['TMDB TV Shows Analysis Dashboard'],
                                style = {'font-family':'Calibri', 'color':'#3A6BAC','textAlign':'center', 'backgroundColor':'F5F5F5'
                                        }),
                                html.Br(),

    html.H2(children = ["Number of Posts By Each Sub-Reddit"],  style = {'font-family':'bradley hand, cursive', 'color':'black','textAlign':'left', 'backgroundColor':'F5F5F5'}),
    dcc.Graph(
        id='life-exp-vs',
        figure=fig,
        style= {
            'backgroundColor':'F5F5F5'
        }
    ),

 html.H2(children = ["Analysis of Hype of Most Popular TMDB TV Shows on Twitter"],  style = {'font-family':'bradley hand, cursive', 'color':'black','textAlign':'left', 'backgroundColor':'F5F5F5'}),
      dcc.Graph(
        id='example-graph',
        figure=fig_twitter,
        style= {
            'backgroundColor':'F5F5F5'
        }
    ),
    
        html.Br(),

    html.H2(children = ["Popularity Predictions of Future TV Shows"],  style = {'font-family':'bradley hand, cursive', 'color':'black','textAlign':'left', 'backgroundColor':'CC0066'}),
    generate_table(df_tmdb),
    html.Br(),
    html.H2(children = ["Time Series Graph of Politics Subreddits"],  style = {'font-family':'bradley hand, cursive', 'color':'black','textAlign':'left', 'backgroundColor':'F5F5F5'}),
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig1,
        style= {
            'backgroundColor':'F5F5F5'
        }
    ),
])


if __name__ == '__main__':
    app.run_server(debug=True)
