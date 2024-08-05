from fastapi import APIRouter
from models.driver import Driver
import pandas as pd
import pandera as pa
from typing import List

router = APIRouter()


@router.get("/drivers", response_model=List[Driver])
def get_drivers():
    df = pd.read_csv("data/drivers.csv")

    drivers = [Driver.from_data(row) for _, row in df.iterrows()]
    return drivers

@router.get("/drivers/{driver}", response_model=Driver)
def get_driver(driver: str):
    df = pd.read_csv("data/drivers.csv")
    driver_data = df[df["driverRef"] == driver].iloc[0]
    return Driver.from_data(driver_data)