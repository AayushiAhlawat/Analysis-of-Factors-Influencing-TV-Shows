
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd


app = Dash(__name__)

df = pd.read_csv('class.csv')
df.columns = ['subreddit', 'no_of_post_by_subreddit']
df = df.drop(labels=0, axis=0)

fig = px.bar(df, x="subreddit", y="no_of_post_by_subreddit",
                 
                 )



#fig1 = px.line(x=[1, 2, 3, 4], y=[3, 5, 4, 8])
#fig.show()


app.layout = html.Div([
    html.H1("No._of_post by each subreddit"),
    dcc.Graph(
        id='life-exp-vs',
        figure=fig
    ),


#dcc.Graph(
 #       id='life-exp-vs-gdp',
  #      figure=fig1
   # )

])





if __name__ == '__main__':
    app.run_server(debug=True)