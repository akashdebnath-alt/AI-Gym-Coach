from backend.database import Base, engine

# Import models so SQLAlchemy knows about all tables
import backend.models

Base.metadata.create_all(bind=engine)

print("Database Created Successfully!")