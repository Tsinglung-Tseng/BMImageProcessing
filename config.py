from skimage import data


class IMG:
    IO={
        'Cell': data.cell,
        'Camera': data.camera,
        'Astronaut': data.astronaut,
        'Coffee': data.coffee
    }
    # (data.cell, 'Cell')
    # CAMERA=data.camera
    # ASTRONAUT=data.astronaut
    # COFFEE=data.coffee
    # PEPPERS='./images/peppers.png'

class SHOW:
    ORIGIN='./tmp_image/origin.png'
    HIST='./tmp_image/hist.png'
    BINARY='./tmp_image/binary.png'
    