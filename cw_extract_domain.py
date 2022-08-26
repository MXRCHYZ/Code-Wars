url = "https://www.cnet.com"
prefix = ["https://", "http://", "www."]
suffix = [".com", ".co", ".ru"]

#remove prefix
def remove_prefix(url):
    for count in range(len(prefix)):
        in_prefix = prefix[count]
        if in_prefix in url:
            break
        else:
            continue
    return url.partition(in_prefix)[2]

while True:
    for i in range(len(prefix)):
        if prefix[i] in url:
            remove_prefix(url)
        else:
            break
    break

print(url)