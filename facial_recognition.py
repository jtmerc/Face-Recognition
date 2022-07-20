# Import Modules
import PIL.Image
import PIL.ImageDraw
import face_recognition

# Python will try to locate any face
picture = face_recognition.load_image_file('ryanalone.jpg')
face_locations = face_recognition.face_locations(picture)
print(face_locations
      )
# How many faces
how_many_faces = len(face_locations)
print("Python located {} face(s) in this image".format(how_many_faces))

# Python will make rectangles around image
pil_picture = PIL.Image.fromarray(picture)
draw_picture = PIL.ImageDraw.Draw(pil_picture)

for faces in face_locations:
    top, right, bottom, left = faces
    draw_picture.rectangle([top, right, bottom, left],
                           outline="green", width=6)

pil_picture.show()
