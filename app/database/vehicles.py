from app.database import get_db


def output_formatter(results):
    out = []
    for result in results:
        vehicle = {
            "driver_id": result[0],
            "first_name": result[1],
            "Last_name": result[2],
            "make": result[3],
            "model": result[4],
            "active": result[5]
        }
        out.append(vehicle)
    return out

 def scan():
    cursor = get_db().execute(
        "SELECT * FROM vehicle WHERE active=1", ()
    )    
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def select_by_id(pk):
    cursor = get_db().execute(
        "SELECT * FROM vehicle WHERE id=?" AND active=1",
        (pk, )
    )
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)

def insert(vehicle_dict):
    value_tuple = (
        vehicle_dict.get("first_name"),
        vehicle_dict.get("last_name"),
        vehicle_dict.get("make"),
        vehicle_dict.get("model")
    )
    statement = """
        INSERT INTO vehicle(
            first_name,
            last_name
            make,
            model
        ) VALUES (?, ?, ?, ?)
    """
    cursor = get_db()
    cursor.execute(statement, value_tuple)
    cursor.commit()
    cursor.close()   

def update(pk, vehicle_data):
    value_tuple = (
        vehicle_data.get("first_name"),
        vehicle_data.get("last_name"),
        vehicle_data.get("make"),
        vehicle_data.get("model"),
        pk
    )
    statement = """
        UPDATE vehicle
        SET first_name = ?,
        last_name = ?,
        make = ?,
        model= ?
        WHERE driver_id = ?
    """
    cursor = get_db()
    cursor.execute(statement, value_tuple)
    cursor.commit()
    cursor.close()

def deactivate(pk):
    cursor = get_db()
    cursor.execute("UPDATE vehicle SET active=0 WHERE driver_id=?", (pk, ))
    cursor.commit()
    cursor.close()         