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

############################################

### Streaming

## Install packages and compilers
# sudo apt install cmake libjpeg9-dev gcc g++

## Download library
# $ cd ~
# $ git clone https://github.com/jacksonliam/mjpg-streamer

## Compile
# $ cd mjpg-streamer/mjpg-streamer-experimental
# $ make
# $ sudo make install

## Code for server
# $ nano mjpg.sh
export STREAMER_PATH=$HOME/mjpg-streamer/mjpg-streamer-experimental
export LD_LIBRARY=$STREAMER_PATH
$STREAMER_PATHj/mjpg_streamer -i "input_raspicam.so -d 200" -o "output_http.so -w $STREAMER_PATH/www"

## Run server
# $ sh mjpg.sh
