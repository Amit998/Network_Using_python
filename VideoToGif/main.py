from moviepy.editor import VideoFileClip

clip=VideoFileClip("test.mp4")

clip.write_gif("mygif.gif")
clip.write_gif("mygif.gif",fps=10)