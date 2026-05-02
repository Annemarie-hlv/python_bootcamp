
from shiny import App, render, ui
from shinywidgets import output_widget, render_widget
import pandas as pd
import numpy as np 
import plotly.express as px

#1 the UI interface 
app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_slider("n", "Number of datapoints", 10, 100, 50),
        ui.input_select("color", "Choose a color", ["blue", "red", "pink", "magenta"])
    ),
    ui.card(
        ui.card_header("MDA Bootcamp Dashboard"),
        output_widget("my_plot")
    )
)


#2 the server logic
def server(input, output, session):
    @render_widget
    def my_plot():
        n = input.n()
        color = input.color()
        data = pd.DataFrame({
            "x" : np.random.rand(n),
            "y" : np.random.rand(n)
        })

        fig = px.scatter(
            data,
            x="x",
            y="y",
            title=f"trend for {n} datapoints",
            color_discrete_sequence=[color]
        )
        return fig

#3 create the app: combine the UI and the server
app= App(app_ui, server)




