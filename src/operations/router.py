import time

from fastapi import APIRouter, Depends, HTTPException
from fastapi_cache.decorator import cache
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from operations.models import operation
from operations.schemas import OperationCreate

router = APIRouter(
    prefix="/operations",
    tags=['Operation'],
)


@router.get("/long_operation")
@cache(expire=30)  # redis cache
def get_long_op():
    time.sleep(2)
    return "Много много данных, которые вычислялись сто лет"


@router.get("")
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):

    try:
        query = select(operation).where(operation.c.type == operation_type)
        result = await session.execute(query)
        return {
                'status': 'success',
                'data': [dict(data._mapping) for data in result.all()],
                'details': None,
        }
    except Exception:

        # log error

        raise HTTPException(
            status_code=500,
            detail={
                'status': 'error',
                'data': None,
                'details': 'Some error.'  # better specify specific exception
            }
        )

@router.post("")
async def add_specific_operation(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    statement = insert(operation).values(**new_operation.dict()) # new_operation.model_dump()
    await session.execute(statement)
    await session.commit()
    return {"status": "success"}
