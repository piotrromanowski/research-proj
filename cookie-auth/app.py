from app import app
from app.utils import login_manager

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
