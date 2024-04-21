
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px



app = Dash(__name__)

df = pd.read_csv('class.csv')
df.columns = ['subreddit', 'no_of_post_by_subreddit']
df = df.drop(labels=0, axis=0)
df2 = pd.read_csv('date_com.csv')
df2.columns = ['date', 'no_of_comments']

fig = px.bar(df, x="subreddit", y="no_of_post_by_subreddit",
                 
                 )



#fig1 = px.line(x=[1, 2, 3, 4], y=[3, 5, 4, 8])
#fig.show()



fig1 = go.Figure(data=go.Scatter(x=df2['date'].astype(dtype=str), 
                                y=df2['no_of_comments'],
                                marker_color='black', text="counts"))
fig1.update_layout({"title": 'Politics subreddtit : time series of comments',
                   "xaxis": {"title":"Time"},
                   "yaxis": {"title":"Total comments"},
                   "showlegend": False})




#fig1 = go.Figure([go.Scatter(x=df2['date'], y=df2['no_of_comments'])])




app.layout = html.Div([
    html.H1("No._of_post by each subreddit"),
    dcc.Graph(
        id='life-exp-vs',
        figure=fig
    ),


dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig1
    )

])





if __name__ == '__main__':
    app.run_server(debug=True)