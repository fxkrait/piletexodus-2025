# 2025-renameAnMovePhoto.sh
# rename photo taken in libreCamera, for ingestion and movement into the piletexodus applicable feed.
# https://stackoverflow.com/questions/1401482/yyyy-mm-dd-format-date-in-shell-script

outputFileName="/data/data/com.termux/files/home/storage/dcim/piletexodus/$(date +%F).jpg"
mv /data/data/com.termux/files/home/storage/dcim/piletexodus/* $outputFileName
