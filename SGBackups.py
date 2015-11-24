import ftputil
import os
import re
import time

FTP_ADDR = None
FTP_USER = None
FTP_PASS = None

backup_pattern = re.compile('wp\.(.*)\.(.*)\.tar\.gz')


def load_config():
    config = ConfigParser.configParser()
    config.read("settings.conf")
    FTP_ADDR = config.get('ftp', 'ftp_addr')
    FTP_USER = config.get('ftp', 'ftp_user')
    FTP_PASS = config.get('ftp', 'ftp_pass')

def get_backups():
    local_files = os.listdir("./Backups")

    with ftputil.FTPHost(FTP_ADDR, FTP_USER, FTP_PASS) as host:
        names = host.listdir(host.curdir)
        for name in names:
            if host.path.isfile(name) and re.match(backup_pattern, name) and name not in local_files:
                print "Downloading: " + name
                host.download(name, 'Backups/' + name)


def main():
    load_config()
    while True:
        get_backups()
        time.sleep(60*60)


if __name__ == "__main__":
    main()
