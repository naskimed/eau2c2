from dash import dcc, html
import datetime as dt
import dash_bootstrap_components as dbc


def create_navbar():

    PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
    
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
                            dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                            dbc.Col(dbc.NavbarBrand("EAU2C2 Dashboard", className="ms-2")),
                        ],
                        align="center",
                        className="g-0",
                    ),
                    href="https://plotly.com",
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
    input_table = html.Div(children=[
    html.H1('Analyzing the Data'),

    html.Div(className="input-section", children=[

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
                        style={'marginBottom': 10, 'marginTop': 10, 'marginRight': 10, 'marginLeft': 10,'width': 200, 'border': '1px solid #ccc','borderRadius': 4, 'padding': '8px 8px','backgroundColor': '#fff', 'textAlign': 'center' },
                    ),
                ]),

                html.Div(className="input-row", children=[
                    html.Label('End Date:'),
                    dcc.DatePickerSingle(
                        id='end-date',
                        min_date_allowed=dt.datetime(1999, 1, 1),
                        max_date_allowed=dt.datetime.today() + dt.timedelta(days=7),
                        style={'marginBottom': 10, 'marginTop': 10, 'marginRight': 10, 'marginLeft': 41,'width': 200, 'border': '1px solid #ccc','borderRadius': 4, 'padding': '8px 8px','backgroundColor': '#fff', 'textAlign': 'center'},
                        
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

    ]),
     html.Button('Run Simulation', id='run-button', className='run-button')
    ]),

    return input_table