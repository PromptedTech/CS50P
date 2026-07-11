# Ask the user to type a file name, then remove extra spaces and make it lowercase
# e.g. "  Photo.PNG  " becomes "photo.png"
name = input("File name: ").strip().lower()

# Check the file extension and print the matching media type (MIME type)
# MIME types tell browsers and apps what kind of file it is

if name.endswith(".gif"):
    print("image/gif")
elif name.endswith(".jpg") or name.endswith(".jpeg"):
    print("image/jpeg")
elif name.endswith(".png"):
    print("image/png")
elif name.endswith(".pdf"):
    print("application/pdf")
elif name.endswith(".txt"):
    print("text/plain")
elif name.endswith(".zip"):
    print("application/zip")
else:
    # Unknown file type — use a generic binary type
    print("application/octet-stream")
