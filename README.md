# Blog-backup
This is a simple script for pulling down WordPress backups from SiteGround.

## Setup
1. Create a backup user in siteground whose root directory is the SiteGround backup directory (e.g. /home/myaccount43/softaculous_backups
2. Create a copy of `settings.conf.sample` named `settings.conf` and add the address, user, and password you configured in step 1.
3. Run the script using `python SGBackups.py`
4. The script will now pull down new backups every hour into `./Backups`.
