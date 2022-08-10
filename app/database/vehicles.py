from app.database import get_db


def output_formatter(results):
    out = []
    for result in results:
        vehicle = {
            "driver": result[0],
            "make": result[1],
            "model": result[2],
        }
        out.append(vehicle)
    return out

def insert(vehicle_dict):
    value_tuple = (
        vehicle_dict.get("driver"),
        vehicle_dict.get("make"),
        vehicle_dict.get("model")
    )
    statement = """
        INSERT INTO vehicle(
            driver,
            make,
            model
        ) VALUES (?, ?, ?)
    """
    cursor = get_db()
    cursor.execute(statement, value_tuple)
    cursor.commit()
    cursor.close()   

def update(pk, vehicle_data):
    value_tuple = (
        vehicle_data.get("driver"),
        vehicle_data.get("make"),
        vehicle_data.get("model"),
        pk
    )
    statement = """
        UPDATE vehicle
        SET driver = ?,
        make = ?,
        model= ?
        WHERE id = ?
    """
    cursor = get_db()
    cursor.execute(statement, value_tuple)
    cursor.commit()
    cursor.close()

def deactivate(pk):
    cursor = get_db()
    cursor.execute("UPDATE vehicle SET active=0 WHERE id=?", (pk, ))
    cursor.commit()
    cursor.close()         