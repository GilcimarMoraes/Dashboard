import dash_bootstrap_components as dbc
import dash
from dash import html

# Criar a instância da aplicação Dash
app = dash.Dash(
    external_stylesheets=[dbc.themes.DARKLY]
)

# Definir o layout da aplicação
app.layout = dbc.Container(
    dbc.Row(
        dbc.Col(html.H1(className='text-center'), width=12)
    ),
    fluid=True
)

# Rodar o servidor
if __name__ == "__main__":
    app.run_server(debug=True, port=8051)
