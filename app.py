from server import application

if __name__ == '__main__':
    application.run(debug=False, host='0.0.0.0', port=80)