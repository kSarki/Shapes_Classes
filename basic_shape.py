class BasicShape:
  def __init__(self):
      pass  # nothing special for now

  def area(self):
      raise NotImplementedError("Subclasses must implement area method")

  def perimeter(self):
      raise NotImplementedError("Subclasses must implement perimeter method")
