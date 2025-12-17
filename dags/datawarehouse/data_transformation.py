from datetime import datetime, timedelta, time


def parse_duration(duration_str):
    # If already converted to a time object (e.g., 00:01:05), convert to timedelta
    if isinstance(duration_str, time):
        return timedelta(
            hours=duration_str.hour,
            minutes=duration_str.minute,
            seconds=duration_str.second,
        )

    # Otherwise assume ISO-8601 duration string like "PT1H2M3S"
    duration_str = duration_str.replace("P", "").replace("T", "")
    components = ["D", "H", "M", "S"]
    values = {"D": 0, "H": 0, "M": 0, "S": 0}

    for component in components:
        if component in duration_str:
            value, duration_str = duration_str.split(component)
            values[component] = int(value)

    return timedelta(
        days=values["D"],
        hours=values["H"],
        minutes=values["M"],
        seconds=values["S"],
    )


def transform_data(row):
    duration_td = parse_duration(row["Duration"])
    row["Duration"] = (datetime.min + duration_td).time()
    row["Video_Type"] = "Shorts" if duration_td.total_seconds() <= 60 else "Normal"
    return row
