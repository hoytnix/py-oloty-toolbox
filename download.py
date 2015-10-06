import sys, requests

def download(url, file_path):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible)'
        }

        r = requests.get(url, headers=headers)
        html = r.content

        with open(file_path, 'wb+') as f:
            f.write(html)

        return file_path
    except:
        print("Unexpected error: %s" % sys.exc_info()[0])
        return False