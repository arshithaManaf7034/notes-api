from app.db.session import engine

try:
    with engine.connect() as conn:
        print("✅ Database connected successfully via SQLAlchemy")
except Exception as e:
    print("❌ Database connection failed:", e)
