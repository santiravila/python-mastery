filename = input("File name: ").strip().lower()

# negative indexing for accessing the last element of the list from split()
extension = filename.split('.')[-1] 

match extension:
    case "gif": 
        print("image/gif")
    case "jpg":
        print("image/jpeg")
    case "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")