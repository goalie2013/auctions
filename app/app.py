from flask import Flask, render_template, request
from .db import get_dataframe_from_db, get_all_tables_from_db, filter_by_time
from datetime import datetime, timedelta
from .map import create_markers

app = Flask(__name__)


@app.get('/')
def index():
    pass

@app.post('/')
def make_markers():
    pass

@app.get('/map')
def mapbox_map():
    """
    Show markers on map w/ optional min_price query parameter
    """

    db_tables = get_all_tables_from_db()
    print('db_tables', db_tables)
    for table_name in db_tables:
        # Grab the (only) table name in the tuple
        print(table_name[0])
        print(type(table_name[0]))
        df = get_dataframe_from_db(table_name[0])
    
        marker_data = create_markers(df)

    # Render the template with marker data
    return render_template('map.html', marker_data=marker_data)


@app.get('/map/timeleft/<days>')
def mapbox_map_time_left(days):
    """
    Filter & show markers for places where time left is less than path parameter value
    """

    # Calculate the total timedelta
    time_delta = timedelta(days=days)
    # Get the current datetime
    current_datetime = datetime.now()
    # Calculate the final datetime
    final_datetime = current_datetime + time_delta

    db_tables = get_all_tables_from_db()
    print('db_tables', db_tables)
    for table_name in db_tables:
        # Grab the (only) table name in the tuple
        print(table_name[0])
        df_time = filter_by_time(table_name[0], final_datetime)
    
        marker_data = create_markers(df_time)

    # Render the template with marker data
    return render_template('map.html', marker_data=marker_data)



if __name__ == "__main__":
    app.run(debug=True)