import os

import server

if __name__ == '__main__':
    # Check if this is a debug server
    flask_env = os.environ.get('FLASK_ENV')
    is_debug = flask_env == 'development'

    server.app.run(debug=is_debug, host='0.0.0.0', threaded=True)
