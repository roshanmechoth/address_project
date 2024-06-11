import traceback
from common.app_response import AppResponse
from common.messages import Messages
from fastapi.exceptions import HTTPException
from common.log_data import ApplicationLogger as applog
from repository.address import *

def add_manager(data):
    """ manager function to perform logic operation
       api name : rename manager
       return json response
     """
    applog.info("add address| Manager Function Started")
    app_response = AppResponse()
    try:
        res = add_db(data)
        if res['code']==200:
            app_response.set_response(200, {}, Messages.SUCCESS, True)
        else:
            app_response.set_response(500, {}, Messages.FAILED, True)
    except Exception as exp:
        raise HTTPException(status_code=500, detail={"code": 500, "message": Messages.FAILED})
    finally:
        return app_response


def update_manager(data,id):
    """ manager function to perform logic operation
       api name : rename manager
       return json response
     """
    applog.info("add address| Manager Function Started")
    app_response = AppResponse()
    try:
        res = update_db(data,id)
        if res['code']==200:
            app_response.set_response(200, {}, Messages.SUCCESS, True)
        else:
            app_response.set_response(500, {}, Messages.FAILED, True)
    except Exception as exp:
        raise HTTPException(status_code=500, detail={"code": 500, "message": Messages.FAILED})
    finally:
        return app_response


def get_manager(id):
    """ manager function to perform logic operation
       api name : rename manager
       return json response
     """
    applog.info("add address| Manager Function Started")
    app_response = AppResponse()
    try:
        res = get_db(id)
        if res['code']==200:
            app_response.set_response(200, res['data'], Messages.SUCCESS, True)
        else:
            app_response.set_response(500, {}, Messages.FAILED, True)
    except Exception as exp:
        raise HTTPException(status_code=500, detail={"code": 500, "message": Messages.FAILED})
    finally:
        return app_response


def delete_manager(id):
    """ manager function to perform logic operation
       api name : rename manager
       return json response
     """
    applog.info("add address| Manager Function Started")
    app_response = AppResponse()
    try:
        res = delete_db(id)
        if res['code']==200:
            app_response.set_response(200, res['data'], Messages.SUCCESS, True)
        else:
            app_response.set_response(500, {}, Messages.FAILED, True)
    except Exception as exp:
        raise HTTPException(status_code=500, detail={"code": 500, "message": Messages.FAILED})
    finally:
        return app_response


def get_address_manager(latitude,longitude,distance):
    """ manager function to perform logic operation
       api name : rename manager
       return json response
     """
    applog.info("add address| Manager Function Started")
    app_response = AppResponse()
    try:
        res = get_address_db(latitude,longitude,distance)
        if res['code']==200:
            app_response.set_response(200, res['data'], Messages.SUCCESS, True)
        else:
            app_response.set_response(500, {}, Messages.FAILED, True)
    except Exception as exp:
        raise HTTPException(status_code=500, detail={"code": 500, "message": Messages.FAILED})
    finally:
        return app_response
