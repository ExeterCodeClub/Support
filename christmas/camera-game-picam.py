import picam
import time

i = picam.takePhoto()
i.save('./before.jpg')

#add disable_camera_led=1 to config.txt to have control over the LED
picam.LEDOn()
print('LED on')
time.sleep(1)
picam.LEDOff()
print('LED off')

#picam.config.imageFX = picam.MMAL_PARAM_IMAGEFX_WATERCOLOUR
picam.config.exposure = picam.MMAL_PARAM_EXPOSUREMODE_AUTO
picam.config.meterMode = picam.MMAL_PARAM_EXPOSUREMETERINGMODE_AVERAGE
picam.config.awbMode = picam.MMAL_PARAM_AWBMODE_SHADE
picam.config.ISO = 0 #auto
picam.config.ISO = 400
picam.config.ISO = 800

picam.config.sharpness = 0               # -100 to 100
picam.config.contrast = 0                # -100 to 100
picam.config.brightness = 50             #  0 to 100
picam.config.saturation = 0              #  -100 to 100
picam.config.videoStabilisation = 0      # 0 or 1 (false or true)
picam.config.exposureCompensation  = 0   # -10 to +10 ?
picam.config.rotation = 0               # 0-359
picam.config.hflip = 0                   # 0 or 1
picam.config.vflip = 0                   # 0 or 1
picam.config.shutterSpeed = 100         # 0 = auto, otherwise the shutter speed in ms

i = picam.takePhoto()
i.save('./after.jpg')

# (width, height, jpg quality)
ii = picam.takePhotoWithDetails(640,480, 85) 

#RGB pixel info
frame1 = picam.takeRGBPhotoWithDetails(width,height)
frame2 = picam.takeRGBPhotoWithDetails(width,height)

#returns RGB pixel list with modified pixels, and the quantity of changed pixels
THRESHOLD=15
(modified,q) = picam.difference(frame1,frame2,THRESHOLD)




#filename = "/tmp/picam-%s.h264" % time.strftime("%Y%m%d-%H%M%S")

# (width, height, duration = 5s)
#picam.recordVideoWithDetails(filename,640,480,5000) 

#picam.config.videoProfile = picam.MMAL_VIDEO_PROFILE_H264_HIGH
#picam.config.videoFramerate = 15
#picam.config.videoBitrate = 17000000

#picam.config.inlineHeaders = 0         # Insert inline headers to stream (SPS, PPS), 0 or 1
#picam.config.quantisationParameter = 0 # Quantisation parameter - quality. Set bitrate 0 and set this for variable bitrate

#picam.config.roi = [0.0,0.0,0.5,0.5]  # Region of interest, normalised coordinates (0.0 - 1.0).
#picam.config.roi = [0.5,0.5,0.25,0.25]


