from zipfile import ZipFile


code = 90052

comments = ""
with ZipFile('channel.zip') as myzip:
    while True:
        with myzip.open(f"{code}.txt", "r") as f:
            data = f.read().decode("utf-8")
            print(data)
            code = data.split()[-1]

            if not code.isdigit():
                break
            comments += myzip.getinfo(f"{code}.txt").comment.decode("utf-8")

print(comments)
