from dash import dcc, html
import datetime as dt
import dash_bootstrap_components as dbc
from PIL import Image


def create_navbar():

    PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
    eau2c2_img = Image.open("assets/images/o2c2.png")

    
    search_bar = dbc.Row(
        [
            dbc.Col(dbc.Input(type="search", placeholder="Search")),
            dbc.Col(
                dbc.Button(
                    "Search", color="primary", className="ms-2", n_clicks=0
                ),
                width="auto",
            ),
        ],
        className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
        align="center",
    )
    
    navbar = dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    dbc.Row(
                        [
                            dbc.Col(html.Img(src=eau2c2_img, height="30px")),
                            dbc.Col(dbc.NavbarBrand("Dashboard", className="ms-2")),
                        ],
                        align="center",
                        className="g-0",
                    ),
                    style={"textDecoration": "none"},
                ),
                dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                dbc.Collapse(
                    dbc.Nav(
                        [
                            dbc.NavItem(dbc.NavLink("Realtime Data", href="/realtime", className="nav-link")),
                            dbc.NavItem(dbc.NavLink("Predictions", href="/predictions", className="nav-link")),
                            dbc.NavItem(dbc.NavLink("Recommendations", href="/recommendations", className="nav-link")),
                        ],
                        className="ms-auto",
                    ),
                    id="navbar-collapse",
                    is_open=False,
                    navbar=True,
                ),
            ]
        ),
        color="dark",
        dark=True,
    )

    return navbar


def create_RealtimeData():
    realtime_content = html.Div( className = "RealtimeTable", children = [
    html.H2("Historical Data", style={'textAlign': 'center'}),

    # Table to display the data
    dcc.Interval(id='interval-component', interval=10 * 1000, n_intervals=0),
    html.Div(id='table-container'),
    html.Link(rel='stylesheet', href='/assets/styles.css'),
    ])

    return realtime_content


def Create_Input_Table():

    pil_img = Image.open("assets/images/LogoDashboard.png")

    input_table = html.Div(className="input-section", children=[

    html.Div(className="behavior-section2", children=[
    html.Img(src=pil_img, style={'width': '50%', 'marginLeft': -25, 'marginBottom': 20,}),

    html.Div(className="description-text", children=[
    html.P("""The Eau2C2 dashboard stands as an innovative and indispensable tool for comprehensively monitoring and analyzing water resources in Tunisia and Canada."""),
    html.P("""At its core, the dashboard harnesses the power of IoT sensors, ensuring that the data presented is not only up-to-date but also derived from a network of intelligent sensors strategically placed to capture diverse facets of water resources. This dynamic integration of real-time data provides users with a holistic view of the current state of water sources."""),
    html.P("""What sets Eau2C2 apart is its utilization of advanced machine learning models, which elevate the platform beyond mere data visualization. These models delve into the intricate patterns and trends within the data, enabling the generation of accurate predictions about future water resource dynamics."""),
    html.P("""Moreover, the dashboard empowers users to formulate informed recommendations, supported by the analytical prowess of these machine learning algorithms. Whether it's analyzing trends, predicting future scenarios, or making strategic decisions for water resource management, Eau2C2 emerges as a cutting-edge solution."""),
    ]),
    ]),

    html.Div(className="behavior-section1", children=[
        html.H1('Analyzing the Data'),
        html.Div(
            className="date-section",
            children=[
                html.H4('Choose the Period:'),

                html.Div(className="input-row", children=[
                    html.Label('Starting Date:'),
                    dcc.DatePickerSingle(
                        id='start-date',
                        min_date_allowed=dt.datetime(1999, 1, 1),
                        max_date_allowed=dt.datetime.today() + dt.timedelta(days=7),
                        style={'marginBottom': 10, 'marginTop': 10, 'marginRight': 10, 'marginLeft': 10,'width': 200, 'borderRadius': 4, 'padding': '8px 4px','backgroundColor': '#ffffff6b', 'textAlign': 'center' },
                    ),
                ]),

                html.Div(className="input-row", children=[
                    html.Label('End Date:'),
                    dcc.DatePickerSingle(
                        id='end-date',
                        min_date_allowed=dt.datetime(1999, 1, 1),
                        max_date_allowed=dt.datetime.today() + dt.timedelta(days=7),
                        style={'marginBottom': 10, 'marginTop': 10, 'marginRight': 10, 'marginLeft': 41,'width': 200, 'borderRadius': 4, 'padding': '8px 2px','backgroundColor': '#ffffff6b', 'textAlign': 'center'},
                        
                    ),
                ]),

            ]),
        

        html.Div(className="place-section", children=[
            html.H4('Choose the Place:'),
            dcc.Dropdown(
                id="place-dropdown",
                options=[
                    {'label': 'Bir Mcherga', 'value': 'BMC'},
                    {'label': 'Canada', 'value': 'CAN'},
                ],
                value='BMC',
            ),
        ]),

        html.Div(className="standalone-switch", children=[
            html.H4('Real Time:'),
            dbc.Switch(
                id='standalone-switch',
                value=True,
                label="Turn on real time data update",
                inputStyle={
                "backgroundColor": "#fa7268",
                "borderColor": "#ea6258",
            },
            ),
        ]),
    html.Button('Start Analyzing', id='run-button', className='run-button'),
    ]),
    ]),

    return input_table