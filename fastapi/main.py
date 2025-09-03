from fastapi import FastAPI, Request

app= FastAPI()

@app.get("/")
def read_root(request: Request):
    host = request.headers.get('Host')
    real_ip = request.headers.get('X-Real-IP')
    forwarded_for = request.headers.get('X-Forwarded-For')
    proto = request.headers.get('X-Forwarded-Proto')

    print(f"--- New Request Received ---")
    print(f"Host: {host}")
    print(f"User's Real IP: {real_ip}")
    print(f"Forwarded For: {forwarded_for}")
    print(f"Original Protocol: {proto}")
    print(f"--------------------------\n")
    return {"message":"Hello from FastAPI behind Nginx"}

@app.get("/author")
def author():
    print(f"--- Someone visited /author ---")
    return {"message":"Atharv Sharma - DevSecOps"}