from flask import Flask, request
app = Flask(__name__)

@app.route('/rest', methods=['GET', 'POST'])
def hello_world():
    data = request.get_json()
    print(data)
    print('----------------------------------------------------------')
    
    '''
    parameter_dict = request.args.to_dict()    
    if len(parameter_dict) == 0:
        f = open("C:/Users/B180093/venvs/test.txt", 'w')
        f.write("No parameter")
        f.close()
        return 'No parameter'

    parameters = ''
    for key in parameter_dict.keys():
        parameters += 'key: {}, value: {}\n'.format(key, request.args[key])

    f = open("C:/Users/B180093/venvs/test.txt", 'w')
    f.write(parameters + "\n" + data['webhookEvent'] + "\n" + data['issue_event_type_name'])
    f.close()
    '''
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9000)
