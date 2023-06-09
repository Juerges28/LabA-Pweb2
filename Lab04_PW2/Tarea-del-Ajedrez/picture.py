from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []
    for value in self.img:
    	vertical.append(value[::-1])
    return vertical

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    horizontal = []
    for row in self.img:
        horizontal.append(row[::-1])
    return Picture(horizontal)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    negative = []
    for row in self.img:
      negative_row = [self._invColor(pixel) for pixel in row]
      negative.append(negative_row)
    return Picture(negative)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    joined_img = []
    for i in range(len(self.img)):
        joined_row = ''.join(self.img[i]) + ''.join(p.img[i])
        joined_img.append(joined_row)
    return Picture(joined_img)

  def up(self, p):
    """ Devuelve una nueva figura poniendo la figura p bajo la figura actual """
    new_img = p.img + self.img
    return Picture(new_img)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la figura actual """
    under_img = []
    for row in p.img:
        under_img.append(p_img)
    for row in self.img:
        under_img.append(self_img)
    return Picture(under_img)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    repeated_img = [row * n for row in self.img]
    return Picture(repeated_img)

  def verticalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual hacia abajo
        la cantidad de veces que indique el valor de n """
    repeated_img = []
    for _ in range(n):
        repeated_img.extend(self.img)
    return Picture(repeated_img)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

