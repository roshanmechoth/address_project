from __future__ import annotations
from fastapi.security import HTTPBearer
auth_scheme = HTTPBearer()
from fastapi import APIRouter, Request,Depends,Query
from fastapi.responses import JSONResponse
from repository.schema import *
from repository.database import get_db
session = get_db()
from services.address_manager import *
address_router = APIRouter(
    prefix='/book'
)

@address_router.post('/addresses/', dependencies=[], tags=["ADDRESS"],
                     response_model =AddressData)
async def add_address(request: Request,data:AddressData):
    """ This api is used to add new address
        Args: Input Parameter
        Returns:
            Response JSON
        """
    try:
        res = add_manager(data)
        if res['code'] == 200:
            applog.info(f'ADDRESS | API executed Successfully')
            return JSONResponse(status_code=res['code'],
                                content={"code": res['code'], "message": res['message'], "data":res['data']})
        else:
            applog.error(f"ADDRESS | Api execution Failed with 500 status code ")
            return JSONResponse(status_code=res['code'],
                                content={"code": res['code'],
                                         "message":res['message']})
    except Exception as exp:
        applog.error("ADDRESS |Exception occured in listing verticals  : \n{0}".format(traceback.format_exc()))
        raise HTTPException(status_code=500, detail={"code": 500, "message": Messages.FAILED})
    finally:
        session.close()
        pass


@address_router.put('/addresses/{id}', dependencies=[], tags=["ADDRESS"],
                     response_model =AddressData)
async def update_address(request: Request,data:AddressData,id:int):
    """ This api is used to update address
        Args: Input Parameter
        Returns:
            Response JSON
        """
    try:
        res = update_manager(data,id)
        if res['code'] == 200:
            applog.info(f'ADDRESS UPDATE | API executed Successfully')
            return JSONResponse(status_code=res['code'],
                                content={"code": res['code'], "message": res['message'], "data":res['data']})
        else:
            applog.error(f"ADDRESS UPDATE | Api execution Failed with 500 status code ")
            return JSONResponse(status_code=res['code'],
                                content={"code": res['code'],
                                         "message":res['message']})
    except Exception as exp:
        applog.error("ADDRESS UPDATE |Exception occured in listing verticals  : \n{0}".format(traceback.format_exc()))
        raise HTTPException(status_code=500, detail={"code": 500, "message": Messages.FAILED})
    finally:
        session.close()
        pass


@address_router.get('/addresses/{id}', dependencies=[], tags=["ADDRESS"])
async def get_address_by_id(request: Request,id:int):
    """ This api is used to update address
        Args: Input Parameter
        Returns:
            Response JSON
        """
    try:
        res = get_manager(id)
        if res['code'] == 200:
            applog.info(f'ADDRESS GET | API executed Successfully')
            return JSONResponse(status_code=res['code'],
                                content={"code": res['code'], "message": res['message'], "data":res['data']})
        else:
            applog.error(f"ADDRESS GET | Api execution Failed with 500 status code ")
            return JSONResponse(status_code=res['code'],
                                content={"code": res['code'],
                                         "message":res['message']})
    except Exception as exp:
        applog.error("ADDRESS GET |Exception occured in listing verticals  : \n{0}".format(traceback.format_exc()))
        raise HTTPException(status_code=500, detail={"code": 500, "message": Messages.FAILED})
    finally:
        session.close()
        pass


@address_router.delete('/addresses/{id}', dependencies=[], tags=["ADDRESS"])
async def delete_address_by_id(request: Request,id:int):
    """ This api is used to update address
        Args: Input Parameter
        Returns:
            Response JSON
        """
    try:
        res = delete_manager(id)
        if res['code'] == 200:
            applog.info(f'ADDRESS DELETE | API executed Successfully')
            return JSONResponse(status_code=res['code'],
                                content={"code": res['code'], "message": res['message'], "data":res['data']})
        else:
            applog.error(f"ADDRESS DELETE | Api execution Failed with 500 status code ")
            return JSONResponse(status_code=res['code'],
                                content={"code": res['code'],
                                         "message":res['message']})
    except Exception as exp:
        applog.error("ADDRESS DELETE |Exception occured in listing verticals  : \n{0}".format(traceback.format_exc()))
        raise HTTPException(status_code=500, detail={"code": 500, "message": Messages.FAILED})
    finally:
        session.close()
        pass


@address_router.get('/retrieve_addresses/', dependencies=[], tags=["ADDRESS"])
async def get_address_by_data(request: Request,latitude: float = Query(..., description="Latitude of the location"),
                                   longitude: float = Query(..., description="Longitude of the location"),
                                   distance: float = Query(..., description="Distance in kilometers"),):
    """ This api is used to update address
        Args: Input Parameter
        Returns:
            Response JSON
        """
    try:
        res = get_address_manager(latitude,longitude,distance)
        if res['code'] == 200:
            applog.info(f'retrieve_addresses  | API executed Successfully')
            return JSONResponse(status_code=res['code'],
                                content={"code": res['code'], "message": res['message'], "data":res['data']})
        else:
            applog.error(f"retrieve_addresses | Api execution Failed with 500 status code ")
            return JSONResponse(status_code=res['code'],
                                content={"code": res['code'],
                                         "message":res['message']})
    except Exception as exp:
        applog.error("retrieve_addresses |Exception occured in listing verticals  : \n{0}".format(traceback.format_exc()))
        raise HTTPException(status_code=500, detail={"code": 500, "message": Messages.FAILED})
    finally:
        session.close()
        pass
