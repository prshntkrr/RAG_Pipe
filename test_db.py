from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql+psycopg://rag_user:Prashant1908@localhost:5432/rag_db"

engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    result = conn.execute(text("SELECT version();"))
    print(result.scalar())
