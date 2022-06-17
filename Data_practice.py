import numpy as np
import pandas as pd
import requests
from dash import Dash, html, dcc
import plotly.express as px
from datetime import date
from dash.dependencies import Input, Output


TOKEN = '2706a3c719c31d14139036e11b37fdf33841f08ea453fe9a1ef6b3d25502867b'

def connection():
    try:
        data = requests.get('https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF43718/datos', headers={'Bmx-Token' : TOKEN})
    except requests.exceptions.Timeout as time_err:
        raise SystemExit(time_err)
    except requests.exceptions.HTTPError as http_err:
        raise SystemExit(http_err)
    except requests.exceptions.ConnectionError as conn_err:
        raise SystemExit(conn_err)
    except requests.exceptions.RequestException as rerr:
        raise SystemExit(rerr)
    
    return data


def savingInformation():
    data = connection()
    json_data = data.json()
    filtered_data = json_data['bmx']['series'][0]['datos']
    df = pd.DataFrame(filtered_data)
    df.to_csv('ExchangeDollar.csv', index = False)
    
def readInformation():
    data = pd.read_csv('ExchangeDollar.csv')
    data['fecha'] = pd.to_datetime(data['fecha'], format = "%d/%m/%Y")
    return data

def firstElement():
    data = readInformation()
    first_element = data.iloc[0]['fecha']
    return first_element

def createPlot():
    app = Dash(__name__)

    df = readInformation()

    fig = px.line(df , x = 'fecha' , y = 'dato' , title = 'Tipo de Cambio')

    app.layout = html.Div(children=[
        html.H1(children = '''Tipo de Cambio'''),
        dcc.Graph(
            id = 'example-graph',
            figure = fig
        ),
        dcc.DatePickerRange(
        id='my-date-picker-range',
        min_date_allowed=date(1995, 8, 5),
        max_date_allowed=date(2017, 9, 19),
        initial_visible_month=date(2017, 8, 5),
        end_date=date(2017, 8, 25)
        ),
        html.Div(id='output-container-date-picker-range')
    ])

    app.run_server(debug = True)

def main():
    print(createPlot())

if __name__ == '__main__':
    main()