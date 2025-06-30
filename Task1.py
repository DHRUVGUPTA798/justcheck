from datetime import datetime


def convert_iso_to_ms(iso_str):
    iso_str = iso_str.replace('Z', '')
    dt = datetime.strptime(iso_str, "%Y-%m-%dT%H:%M:%S.%f")
    return int(dt.timestamp() * 1000)


def unify_data(record):
    if 'id' in record:  # Model A
        return {
            "user_id": record["id"],
            "full_name": f'{record["first_name"]} {record["last_name"]}',
            "birth_timestamp_ms": convert_iso_to_ms(record["dob"])
        }
    else:  # Model B
        return {
            "user_id": record["user_id"],
            "full_name": record["name"],
            "birth_timestamp_ms": convert_iso_to_ms(record["birthdate"])
        }


modelA = [{
    "id": 1,
    "first_name": "Raj",
    "last_name": "Verma",
    "dob": "1990-01-01T00:00:00.000Z"
}]
modelB = [{
    "user_id": 
    "name": "Sneha Gupta",
    "birthdate": "1995-03-21T00:00:00.000Z"
}]

final_output = [unify_data(d) for d in modelA + modelB]
print(final_output)
