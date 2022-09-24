import urllib3, json, os

TOKEN = "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" #os.getenv('github_token')
OWNER = "copyPasteNinja"
REPO = "python-101"
PATH = "everything_is_awesome.py"

"""
curl -X PUT -H "Accept: application/vnd.github+json" 
    -H "Authorization: Bearer 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" https://api.github.com/repos/copyPasteNinja/python-101/contents/new_file 
    -d '{"message":"my commit message via api","committer":{"name":"Abdul Sharif","email":"abdugofir00@gmail.com"},"content":"bXkgbmV3IGZpbGUgY29udGVudHM="}'
"""


def commit():
    http = urllib3.PoolManager()

    # url = 'https://api.github.com/repos/%s/%s/contents/%s' % (OWNER, REPO, PATH)
    url = 'https://api.github.com/repos/copyPasteNinja/python-101/contents/new_file_33'
    header = {"Accept": "application/vnd.github+json", "Authorization": "Bearer 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"}
    data = {"message": "my commit message via api", "committer": {"name": "Abdul Sharif", "email": "abdugofir00@gmail.com"},"content": "Abdul_was_here"}
    encoded_data = json.dumps(data).encode('utf-8')
    
    r = http.request('POST', url, headers=header, body=encoded_data)
    resp = json.loads(r.data.decode('utf-8'))
    print(r.data)


commit()