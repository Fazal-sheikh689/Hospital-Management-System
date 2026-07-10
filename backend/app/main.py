# from fastapi import FastAPI

# app = FastAPI(
#     title="Hospital Management System API",
#     version="1.0.0",
#     description="Backend API for Hospital Management System",
# )

# @app.get("/")
# def root():
#     return {
#         "message": "Hospital Management System API is Running Successfully!"
#     }



# from fastapi import FastAPI
# from app.core.config import settings

# app = FastAPI()


# @app.get("/")
# def root():
#     return {
#         "database": settings.DB_DATABASE,
#         "server": settings.DB_SERVER
#     }



from fastapi import FastAPI

from app.api.routes import roles
from app.core.config import settings

app = FastAPI(
    title="Hospital Management System API",
    version="1.0.0"
)

app.include_router(roles.router)


@app.get("/")
def root():
    return {
        "message": "Hospital Management System API Running",
        "database": settings.DB_DATABASE,
        "server": settings.DB_SERVER
    }