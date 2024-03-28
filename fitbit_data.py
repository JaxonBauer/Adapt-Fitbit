import requests
import time
import oauth2 as oauth2
from pprint import pprint
from math import ceil
import json
import csv

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get access_token and user_id from environment variables
access_token = os.getenv('ACCESS_TOKEN')
user_id = os.getenv('USER_ID')
user_key = os.getenv('USER_KEY')

# Make the API request for heart rate data
heart_rate_request = requests.get(
    'https://api.fitbit.com/1/user/'+user_id+'/activities/heart/date/today/30d.json',
    headers={'Authorization': 'Bearer ' + access_token}
)

# Make the API request for sleep data
sleep_request = requests.get(
    'https://api.fitbit.com/1.2/user/'+user_id+'/sleep/date/2024-03-25.json',
    headers={'Authorization': 'Bearer ' + access_token}
)

# Check if the request was successful
if heart_rate_request.status_code == 200:
    # Extract relevant data from the JSON response
    heart_rate_data_list = heart_rate_request.json()['activities-heart']

    # Create an HTML string to store the content
    html_content = '''
    <html>
    <head>
        <title>Heart Rate Data</title>
        <link rel="stylesheet" href="app.css">
        <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    </head>
    <body>
    <h1>Heart Rate Data - 
    '''

    html_content += user_key + '</h1>'

    # Iterate over each entry in the list
    for heart_rate_data in heart_rate_data_list:
        # Add date to HTML
        html_content += f'<h2>Date: {heart_rate_data["dateTime"]}</h2>'
        
        # Check if resting heart rate is available
        try:
            html_content += f'<p>Resting Heart Rate: {heart_rate_data["value"].get("restingHeartRate", "Not available")}</p>'
        except KeyError:
            html_content += '<p>Resting Heart Rate: Not available</p>'
        
        # Add heart rate zones to HTML in a table
        html_content += '<div class="container">'
        html_content += '<div class="table-container">'
        html_content += '<table border="1">'
        html_content += '<tr><th>Name</th><th>Minutes</th><th>Min</th><th>Max</th><th>Calories Out</th></tr>'
        for zone in heart_rate_data['value']['heartRateZones']:
            html_content += '<tr>'
            html_content += f'<td>{zone.get("name", "Not available")}</td>'
            html_content += f'<td>{zone.get("minutes", "Not available")}</td>'
            html_content += f'<td>{zone.get("min", "Not available")}</td>'
            html_content += f'<td>{zone.get("max", "Not available")}</td>'
            # Round up the caloriesOut value to the nearest whole number
            calories_out_rounded = ceil(zone.get("caloriesOut", 0))
            html_content += f'<td>{calories_out_rounded}</td>'
            html_content += '</tr>'
        html_content += '</table>'
        html_content += '</div>'  # Close table-container
        
        # Add the chart div
        html_content += '<div class="chart-container">'
        html_content += f'<div id="chart_div_{heart_rate_data["dateTime"]}" class="chart"></div>'
        html_content += '</div>'  # Close chart-container
        html_content += '</div>'  # Close container

        # Prepare the JavaScript code for generating the chart
        chart_script = f'''
        <script type="text/javascript">
            google.charts.load("current", {{ packages: ["corechart"] }});
            google.charts.setOnLoadCallback(drawChart);

            function drawChart() {{
                var data = new google.visualization.DataTable();
                heart_data_processing(data, {heart_rate_data['value']['heartRateZones']});
                var options = {{
                    title: "Calories Burned By Activity Zone",
                    width: 400,
                    height: 300,
                }};
                var chart = new google.visualization.PieChart(document.getElementById("chart_div_{heart_rate_data['dateTime']}"));
                chart.draw(data, options);
            }}

            function heart_data_processing(result_data, heart_rate_data) {{
                var data = google.visualization.arrayToDataTable([
                    ["Element", "Calories"],
                    ["Out of Range", 0],
                    ["Fat Burn", 0],
                    ["Cardio", 0],
                    ["Peak", 0],
                ]);

                heart_rate_data.forEach(function(zone) {{
                    switch (zone.name) {{
                        case "Out of Range":
                            data.setValue(0, 1, Math.round(zone.caloriesOut));
                            break;
                        case "Fat Burn":
                            data.setValue(1, 1, Math.round(zone.caloriesOut));
                            break;
                        case "Cardio":
                            data.setValue(2, 1, Math.round(zone.caloriesOut));
                            break;
                        case "Peak":
                            data.setValue(3, 1, Math.round(zone.caloriesOut));
                            break;
                        default:
                            break;
                    }}
                }});

                result_data.addColumn("string", "Element");
                result_data.addColumn("number", "Calories");
                result_data.addRows([
                    ["Out of Range", data.getValue(0, 1)],
                    ["Fat Burn", data.getValue(1, 1)],
                    ["Cardio", data.getValue(2, 1)],
                    ["Peak", data.getValue(3, 1)],
                ]);
            }}
        </script>
        '''

        # Add the chart script
        html_content += chart_script

    # Close the body and HTML tags
    html_content += '</body></html>'

    # Write the HTML content to a file
    with open('heart_rate_data.html', 'w') as f:
        f.write(html_content)

    print("HTML file 'heart_rate_data.html' created successfully.")

else:
    print("Failed to retrieve data. Status code:", heart_rate_request.status_code)




# Check if the request was successful
if sleep_request.status_code == 200:
    # Extract relevant data from the JSON response
    sleep_data_list = sleep_request.json()['sleep']

    # Create an HTML string to store the content
    html_content = '''
    <html>
    <head>
        <title>Sleep Data</title>
        <link rel="stylesheet" href="app.css">
        <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    </head>
    <body>'''

    # Iterate over each entry in the list
    for sleep_data in sleep_data_list:
        # Add date to HTML
        html_content += f'<h2>Date of Sleep: {sleep_data["dateOfSleep"]}</h2>'
        
        html_content += '<div class="container">'
        # Add sleep summary to HTML
        html_content += '<div>'
        html_content += '<p>Sleep Summary:</p>'
        html_content += '<ul>'
        html_content += f'<li>Total Minutes Asleep: {sleep_data["minutesAsleep"]}</li>'
        html_content += f'<li>Total Time in Bed: {sleep_data["timeInBed"]}</li>'
        html_content += '</ul>'

        # Add sleep stages summary to HTML
        html_content += '<p>Sleep Stages Summary:</p>'
        html_content += '<ul>'
        for stage, value in sleep_data['levels']['summary'].items():
            html_content += f'<li>{stage.capitalize()}: {value["minutes"]} minutes</li>'
        html_content += '</ul></div>'

        # Add the chart div
        html_content += '<div class="chart-container">'
        html_content += f'<div id="chart_sleep_div_{sleep_data["dateOfSleep"]}" class="chart"></div>'
        html_content += '</div></div>'  # Close chart-container

        # Prepare the JavaScript code for generating the chart
        chart_script = f'''
        <script type="text/javascript">
            google.charts.load("current", {{ packages: ["corechart"] }});
            google.charts.setOnLoadCallback(drawSleepChart);

            function drawSleepChart() {{
                var data = new google.visualization.DataTable();
                sleepDataProcessing(data, {json.dumps(sleep_data['levels']['summary'])});
                var options = {{
                    title: "Sleep Stages",
                    width: 400,
                    height: 300,
                }};
                var chart = new google.visualization.PieChart(document.getElementById("chart_sleep_div_{sleep_data["dateOfSleep"]}"));
                chart.draw(data, options);
            }}

            function sleepDataProcessing(result_data, sleep_data) {{
                result_data.addColumn("string", "Stage");
                result_data.addColumn("number", "Minutes");
                var stages = Object.keys(sleep_data);
                stages.forEach(function(stage, index) {{
                    result_data.addRow([stage, sleep_data[stage]["minutes"]]);
                }});
            }}
        </script>
        '''

        # Add the chart script
        html_content += chart_script
        html_content += '<br>'

        # Add sleep stages data to HTML in a table
        html_content += '<table border="1">'
        html_content += '<tr><th>Date/Time</th><th>Level</th><th>Minutes</th></tr>'
        for level_data in sleep_data['levels']['data']:
            html_content += '<tr>'
            html_content += f'<td>{level_data["dateTime"]}</td>'
            html_content += f'<td>{level_data["level"].capitalize()}</td>'
            html_content += f'<td>{level_data["seconds"] / 60}</td>'
            html_content += '</tr>'
        html_content += '</table>'

    # Close the body and HTML tags
    html_content += '</body></html>'

    # Write the HTML content to a file
    with open('sleep_data.html', 'w') as f:
        f.write(html_content)

    print("HTML file 'sleep_data.html' created successfully.")

else:
    print("Failed to retrieve data. Status code:", sleep_request.status_code)
