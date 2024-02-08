import subprocess
import jack  # For Jack integration (optional)

# Replace with your desired device name or JACK client name
input_device = "Line In"

# Set output filename and desired format (adjust as needed)
output_file = "recording.wav"  # Common audio format

# Basic ffmpeg command for recording
base_command = [
    "ffmpeg", "-f", "jack", "-i", input_device, "-t", "00:05:00",  # Record for 5 minutes
    output_file
]

# Optional: Use JACK client name if you have Jack integration
if jack.exists():
    client = jack.Client("MyRecordingClient")
    client.activate()
    base_command = [
        "ffmpeg", "-f", "jack", "-i", f"system:{client.name()}/{input_device}", "-t", "00:05:00",
        output_file
    ]

# Execute the ffmpeg command
subprocess.run(base_command)

# Optional: Close Jack client if used
if jack.exists():
    client.deactivate()
