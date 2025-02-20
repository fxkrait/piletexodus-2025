# 2025-photo-test.sh
# Take a series of photos, bright contrast because for some reason termux-camera-photo gives dark photos, and save them into photos/
# https://stackoverflow.com/questions/11162049/using-a-count-variable-in-a-file-name
# https://dominoc925.blogspot.com/2012/05/adjust-brightness-and-contrast-of.html
rm -R photos
mkdir photos
cd photos

for i in $(seq 1 3);
do
    filename="file$i"
    jpg=".jpg"
    brighter="-brighter"
    termux-camera-photo -c 1 "$filename$jpg"
    magick convert -brightness-contrast 50x20 "$filename$jpg" "$filename$brighter$jpg"
    sleep 10 # pause 10 seconds
done

