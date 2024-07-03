class Ball:

  def __init__(self, canvas, x, y, diameter, xVelocity, yVelocity, color):
    self.canvas = canvas
    self.image = canvas.create_oval(x, y, diameter, diameter, fill=color)
    self.xVelocity = xVelocity
    self.yVelocity = yVelocity
  
  def move(self):
    coordinates = self.canvas.coords(self.image)
    print(coordinates)
    if (coordinates[2] >= self.canvas.winfo_width()) or (coordinates[0] < 0):
      self.xVelocity = -1 * self.xVelocity
    if (coordinates[3] >= self.canvas.winfo_height()) or (coordinates[1] < 0):
      self.yVelocity = -1 * self.yVelocity
    
    self.canvas.move(self.image, self.xVelocity, self.yVelocity)
    

    