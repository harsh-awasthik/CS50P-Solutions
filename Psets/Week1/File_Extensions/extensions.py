File = input("File name: ").strip()
extnsn = File[File.rfind("."):].lower()

match extnsn:
    case ".jpg" | ".jpeg":
        print("image/jpeg")
    case ".gif":
        print("image/gif")
    case ".txt":
        print("text/plain")
    case ".png":
        print("image/png")
    case ".pdf":
        print("application/pdf")
    case ".zip":
        print("application/zip")
    case _:
        print("application/octet-stream")
