# 2025-photo-test64.sh
# Take a series of photos, bright contrast because for some reason termux-camera-photo gives dark photos, and save them into photos/
# https://stackoverflow.com/questions/11162049/using-a-count-variable-in-a-file-name
# https://dominoc925.blogspot.com/2012/05/adjust-brightness-and-contrast-of.html
rm -R photos64
mkdir photos64
cd photos64

for i in $(seq 1 64);
do
    filename="file$i"
    jpg=".jpg"
    brighter="-brighter"
    termux-camera-photo -c 1 "$filename$jpg"
    sleep 5 # pause 10 seconds
done

