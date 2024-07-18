ffmpeg -y -i input.mp4 -vf "scale=80:60:force_original_aspect_ratio=decrease,pad=80:60:(ow-iw)/2:(oh-ih)/2,fps=3" -an video.mp4
