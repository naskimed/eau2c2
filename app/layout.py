from dash import dcc, html
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
    html.H2("Historical Data"),
    
    # Table to display the data
    dcc.Interval(id='interval-component', interval=10 * 1000, n_intervals=0),
    html.Div(id='table-container')
    ])

    return realtime_content