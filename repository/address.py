import traceback
from fastapi.exceptions import HTTPException
from common.app_response import AppResponse
from common.messages import Messages
from repository.database import get_db
session = get_db()
from repository.models import Address
from common.utilities import calculate_distance

def add_db(data):
    app_response = AppResponse()
    try:
        create_address = Address(street=data.street,city=data.city,latitude=data.latitude,longitude=data.longitude)
        session.add(create_address)
        app_response.set_response(200, {}, Messages.SUCCESS, False)
    except Exception as exp:
        raise HTTPException(status_code=500, detail={"code": 500, "message": Messages.FAILED})
    finally:
        session.commit()
        return app_response


def update_db(data,id):
    app_response = AppResponse()
    try:
        db_address = session.query(Address).filter(Address.id == id).first()
        if db_address is None:
            app_response.set_response(404, {}, Messages.FAILED, False)
        db_address.street = data.street
        db_address.city = data.city
        db_address.latitude = data.latitude
        db_address.longitude = data.latitude
        app_response.set_response(200, {}, Messages.SUCCESS, False)
    except Exception as exp:
        raise HTTPException(status_code=500, detail={"code": 500, "message": Messages.FAILED})
    finally:
        session.commit()
        return app_response

def get_db(id):
    app_response = AppResponse()
    try:
        get_address = session.query(Address).filter(Address.id == id).first()
        if get_address is None:
            app_response.set_response(404, {}, Messages.FAILED, False)
        else:
            data_address = {
                "street" :get_address.street,
                "city" :get_address.city,
                "latitude" :get_address.latitude,
                "longitude":get_address.longitude
            }
        app_response.set_response(200, data_address, Messages.SUCCESS, False)
    except Exception as exp:
        raise HTTPException(status_code=500, detail={"code": 500, "message": Messages.FAILED})
    finally:
        session.commit()
        return app_response

def delete_db(id):
    app_response = AppResponse()
    try:
        get_address = session.query(Address).filter(Address.id == id).first()
        if get_address:
            session.delete(get_address)
            app_response.set_response(200, {}, Messages.SUCCESS, False)
        else:
            app_response.set_response(404, {}, Messages.FAILED, False)
    except Exception as exp:
        raise HTTPException(status_code=500, detail={"code": 500, "message": Messages.FAILED})
    finally:
        session.commit()
        return app_response

def get_address_db(latitude,longitude,distance):
    app_response = AppResponse()
    try:
        addresses = session.query(Address).all()
        within_distance = []
        for address in addresses:
            if calculate_distance(latitude, longitude, address.latitude, address.longitude) <= distance:
                within_distance.append(address)

        data_final =[]
        for add in within_distance:
            data_set ={
                "street" : add.street,
                "city":add.city,
            }
        app_response.set_response(200,data_set, Messages.SUCCESS, False)
    except Exception as exp:
        raise HTTPException(status_code=500, detail={"code": 500, "message": Messages.FAILED})
    finally:
        session.commit()
        return app_response

