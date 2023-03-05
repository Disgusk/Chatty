import moviepy.editor as moviepy

clip = moviepy.VideoFileClip("test.webm")    
clip.write_audiofile("test.wav")