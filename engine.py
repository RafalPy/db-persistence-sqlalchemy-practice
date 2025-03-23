from sqlalchemy import create_engine

user = input("Enter DB username: ")
password = input("Enter DB password: ")

engine = create_engine(f'postgresql://{user}:{password}@localhost:5432/sqlalchemy')



