import dash_html_components as html
import layouts.style.style as style
from tools.calendar_generation import calendar_config, desk_combobox
import dash_core_components as dcc


def change_calendar_content():
    """
    Create layout for calendar

    :return: Layout with 1 second refresh interval
    :rtype: dash.development.base_component.ComponentMeta
    """
    result = calendar_config()
    if result[0] is not None:
        return html.Div([
            dcc.ConfirmDialog(
                             id='confirm-good',
                             message='Event added',
            ),
            dcc.ConfirmDialog(
                             id='confirm-bad',
                             message='There was an error during adding an event. Please check server logs'
                             ' for an error.',
            ),
            dcc.ConfirmDialog(
                             id='confirm-reserved',
                             message='This desk is already taken. Please reserve another or try again later',
            ),
            html.Iframe(
                       src=result[0],
                       width='1000',
                       height='600'
            ),
            html.H4('Event title'),
            dcc.Dropdown(
                id='desk-choose',
                options=desk_combobox(),
                searchable=False,
            ),
            html.H4('Choose a date of a reservation'),
            html.Div([
                    dcc.DatePickerRange(
                                       id='date-picker-range'
                    )
            ], style={'margin': '10px 5px 10px 5px'}),
            html.H4('Hour (start and end)  of reservation:',
                    style={'margin': '20px 5px 20px 5px'}),
            dcc.RangeSlider(
                           id='hour-slider',
                           count=1,
                           min=0,
                           max=23,
                           step=1,
                           marks={
                                 0: '0',
                                 6: '6',
                                 12: '12',
                                 18: '18',
                                 23: '23'
                           },
                           value=[0, 23]
                           ),
            html.Div(id='divider',
                     style={'margin': '20px 5px 20px 5px'}),
            html.H4('Minutes (start and end) of reservation',
                    style={'margin': '20px 5px 20px 5px'}),
            dcc.RangeSlider(
                           id='minute-slider',
                           count=1,
                           min=0,
                           max=59,
                           step=1,
                           marks={
                                 0: '0',
                                 15: '15',
                                 30: '30',
                                 45: '45',
                                 59: '59'
                           },
                           value=[0, 59]
            ),
            html.Div(id='divider',
                     style={'margin': '40px 5px 40px 5px'}),
            html.Button(
                       id='time-submit-button',
                       n_clicks=0,
                       children='Add an event'
            )], style={'margin': style.PADDING})
    else:
        return html.Div([
            html.H4('There was an error during reading config.yml file. Please check if file exists'
                    '  and if configuration is written properly.')])
