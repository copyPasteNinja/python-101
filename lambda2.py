import urllib3, json, os, requests, base64, time
## GET TOKEN FROM ENV ## 
TOKEN = os.getenv('github_token')
OWNER = "org-or-username"
REPO = "repo-name"
PATH = "/path/to/file"
NAME = "Itachi Uchiha"
EMAIL = "example@gmail.com"


def get_sha(file_name):
    headers={"Accept": "application/vnd.github+json", "Authorization": "Bearer %s" % TOKEN}
    url = 'https://api.github.com/repos/%s/%s/contents/%s' % (OWNER, REPO, file_name)
    r = requests.get(url, headers=headers)
    sha = r.json()['sha']

    return sha

def lambda_handler(context, event):
    sha = get_sha(file_name=PATH)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)

    f = open(PATH, "a")
    f.write("timeStamp "+current_time+ "\n")
    f.close()
    
    ENCODING = 'utf-8'
    with open(PATH, 'rb') as f:
        byte_content = f.read()
        base64_bytes = base64.b64encode(byte_content)
        base64_string = base64_bytes.decode(ENCODING)
        payload = {"message": "Add text.txt", "author": {"name": NAME, "email": EMAIL}, "content": base64_string, "sha": sha}
        result = requests.put("https://api.github.com/repos/%s/%s/contents/%s" % (OWNER, REPO, PATH), 
                            headers={"Accept": "application/vnd.github+json", "Authorization": "Bearer %s" % TOKEN}, 
                            json=payload)
        print(result.json())

lambda_handler()