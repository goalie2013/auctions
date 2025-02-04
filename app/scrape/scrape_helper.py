from datetime import datetime, timedelta

def get_datetime(row, time_col: int) -> datetime:
    """
    For each row in HTML table, find the column (<td>) with the time in format 'XXd XXh'
    Get the date from now from str -> timedelta -> datetime 
    """
    # Find all cells in the row
    cells = row.find_all('td')
    # Check if there are cells in the row
    if cells:
        # Extract the content of the second cell (assuming it contains the time string)
        time_string = cells[time_col].text.strip()
        # Split the time string to extract days and hours
        days, hours = time_string.split()
        # Extract numerical values
        days = int(days[:-1])
        hours = int(hours[:-1])
        # Calculate the total timedelta
        time_delta = timedelta(days=days, hours=hours)
        # Get the current datetime
        current_datetime = datetime.now()
        # Calculate the final datetime
        final_datetime = current_datetime + time_delta
        print("Final Datetime:", final_datetime)

        return final_datetime
