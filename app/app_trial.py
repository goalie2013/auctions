from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta
from db import get_dataframe_from_db, get_all_tables_from_db, filter_by_time
from map import create_markers

app = Flask(__name__)


@app.get('/')
def index():
    return render_template('index.html')

@app.post('/')
def make_markers():
    pass

@app.get('/map')
def mapbox_map():
    """
    Show markers on map on first load
    """
    print('Running mapbox_map()')

    try:

        df = get_dataframe_from_db('new_ca_kern_trial')
    
        marker_data = create_markers(df)

        print(marker_data)
    
    except Exception as error:
        print('Error in app.get(/map): ', error)

    # Render the template with marker data
    return render_template('map.html', marker_data=marker_data)

@app.get('/map/filters')
def mapbox_map_filters():
    """
    Show markers on map w/ optional min_price & datetime query parameters
    """
    print('Running mapbox_map_filters()')

    try:
        min_bid_price_filter = float(request.args.get('price', '0'))
        bid_date_filter = request.args.get('date', None)

        df = get_dataframe_from_db('new_ca_kern_trial')
    
        marker_data = create_markers(df, min_bid_price_filter, bid_date_filter)

        print(marker_data)
    
    except Exception as error:
        print('Error in app.get(/map/filters): ', error)

    # Render the template with marker data
    #return render_template('map.html', marker_data=marker_data)
    return jsonify(marker_data)




@app.get('/map/timeleft/<days>')
def mapbox_map_time_left(days):
    """
    Filter & show markers for places where time left is less than path parameter value
    """
    
    #date = row['Auction Time']

    # Calculate the total timedelta
    time_delta = timedelta(days=days)
    # Get the current datetime
    current_datetime = datetime.now()
    # Calculate the final datetime
    final_datetime = current_datetime + time_delta
    df_time = filter_by_time('kern_ca_temp', final_datetime)
    
    marker_data = create_markers(df_time)

    # Render the template with marker data
    return render_template('map.html', marker_data=marker_data)



if __name__ == "__main__":
    app.run(debug=True, port=8000)