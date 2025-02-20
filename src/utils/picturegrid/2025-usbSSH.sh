# https://medium.com/@baradhiren07/access-termux-from-your-laptop-using-usb-2ceb00c83469
# enable usb debugging on android phone, have adb on computer.
# https://glow.li/posts/access-termux-via-usb/
adb forward tcp:8022 tcp:8022 && adb forward tcp:8080 tcp:8080&& ssh localhost -p 8022
