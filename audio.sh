

device_name = "alsa_input.pci-0000_00_1b.0.analog-stereo"

path = "~/audiorec/out.mp3"

ffmpeg -f pulse -i $device_name -codec:a libmp3lame -qscale:a 2 ~/recording.mp3