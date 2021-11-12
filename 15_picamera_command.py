### Take picture and video

## Take picture after 5 seconds
# $ raspistill -o <filename>.jpg

## Take picture after 3 seconds
# $ raspistill -t 3000 -o <filename>.jpg

## Take video
# $ raspivid -o <filename>.h264
## Or
# $ raspivid -o <filename>.mpeg

## Take video for 10 seconds in demo
# $ raspivid -o <filename>.h264 -t 10000 -d

## Other options
# -w: width
# -h: height
# -q: quality(0~100)
# -br: brightness(0~100)
# -k: shot using 'Enter Key'

## Check video
# $ omxplayer <filename>.h264
# $ omxplayer <filename>.mpeg

############################################

### Streaming

## Install packages and compilers
# sudo apt update && sudo apt upgrade
# sudo apt install cmake libjpeg8-dev gcc g++

## Download library
# $ cd ~
# $ git clone https://github.com/jacksonliam/mjpg-streamer

## Compile and install
# $ cd mjpg-streamer/mjpg-streamer-experimental
# $ make
# $ sudo make install

## Code for running
# $ nano mjpg.sh
# export STREAMER_PATH=$HOME/mjpg-streamer/mjpg-streamer-experimental
# export LD_LIBRARY=$STREAMER_PATH
# $STREAMER_PATH/mjpg_streamer -i "input_raspicam.so" -o "output_http.so -w $STREAMER_PATH/www"

## Run
# $ sh mjpg.sh

## Watch streaming: type in browser
# localhost:8080               
# <raspberrypi_ip_address>:8080