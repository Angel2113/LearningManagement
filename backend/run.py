import sys
import os
import uvicorn

# Add the current directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

if __name__ == "__main__":
    # Run the application using uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)