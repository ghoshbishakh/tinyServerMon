from flask import Flask
app = Flask(__name__)

def get_users_space():
    users_space_list = []
    users_space_file = open('users_space.txt')
    users_space_text = users_space_file.read()
    users_space_file.close()
    users_space_text = users_space_text.strip().split("\n")
    users_space_text = [a.split(" ") for a in users_space_text]
    for line in users_space_text:
        print(line[0])
        users_space_list.append([(int(line[0])/(1024*1024)), line[1]])
    return users_space_list


@app.route('/space')
def space():
    return {'users_space' : get_users_space()}


@app.route('/space')
def space():
    return {'users_space' : get_users_space()}


if __name__ == '__main__':
    app.run()