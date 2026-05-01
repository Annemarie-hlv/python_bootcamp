
from shiny import App, render, ui

#1 the UI interface 
app_ui = ui.page_fluid(
    ui.h1("My MDA Dashboard"),
    ui.input_text("name_input", "what is your name?", value= "Anna"),
    ui.output_text("greeting")
)

#2 the server logic
def server(input, output, session):
    @render.text
    def greeting():
        return f"Hello {input.name_input()}! Welcome to the MDA Bootcamp Dashboard :)"

#3 create the app: combine the UI and the server
app= App(app_ui, server)




