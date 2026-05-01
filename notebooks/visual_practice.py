import pandas as pd
import plotly.express as px

data = {
    'Student': ['Annemarie', 'Teammate1', 'Teammate2'],
    'Score': [95, 88, 92]
}
df = pd.DataFrame(data)

fig = px.bar(df, x='Student', y='Score', title='Bootcamp Scores', color='Student')

fig.show()