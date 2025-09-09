from ftplib import FTP

# FTP Server details (public test server)
FTP_HOST = "ftp.dlptest.com"
FTP_USER = "dlpuser"
FTP_PASS = "rNrKYTX9g7z3RgJRmxWuGHbeu"


def connect_ftp():
    """Connect to FTP server and return FTP object."""
    ftp = FTP(FTP_HOST)
    ftp.login(user=FTP_USER, passwd=FTP_PASS)
    print(f"Connected to FTP server: {FTP_HOST}\n")
    return ftp


def upload_file(ftp, filename):
    """Upload a file to FTP server."""
    with open(filename, "w") as f:
        f.write("This is a test file uploaded using Python FTP client.")

    with open(filename, "rb") as f:
        ftp.storbinary(f"STOR {filename}", f)
    print(f"File '{filename}' uploaded successfully!")


def download_file(ftp, remote_file, local_file):
    """Download a file from FTP server and verify its content."""
    with open(local_file, "wb") as f:
        ftp.retrbinary(f"RETR {remote_file}", f.write)
    print(f"File '{remote_file}' downloaded successfully as '{local_file}'!")

    # Verify content
    with open(local_file, "r") as f:
        content = f.read()
        print("Downloaded file content:", content)


def list_directory(ftp):
    """List contents of FTP directory."""
    print("\nDirectory listing on FTP server:")
    ftp.retrlines("LIST")


def main():
    try:
        ftp = connect_ftp()
        # Upload file
        upload_file(ftp, "upload_test.txt")
        # Download file
        download_file(ftp, "upload_test.txt", "download_test.txt")
        # List directory
        list_directory(ftp)
        # Close connection
        ftp.quit()
        print("\nConnection closed.")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
