#                        Example for <Handler> Pattern Design
#                    ********************************************
from abc import ABC, abstractmethod

ALLOWED = ['html', 'mp3', 'mp4']


class AbstractRenderer(ABC):
  @abstractmethod
  def render(self):
    pass


class HtmlRenderer(AbstractRenderer):
  def render(self):
    print('Render from Html Renderer')


class Mp3Renderer(AbstractRenderer):
  def render(self):
    print('Render from Mp3 Renderer')


class Mp4Renderer(AbstractRenderer):
  def render(self):
    print('Render from Html Streamer')


class FileHandler:
  def __init__(self, filename):
    self.filename = filename

  def extension(self):
    return self.filename.split('.')[-1]

  @classmethod
  def create(cls, filename):
    if filename.split('.')[-1] not in ALLOWED:
      print('Not allowed')

    return cls(filename)

  def render(self):
    allowed_dict = {
      'html': HtmlRenderer,
      'mp3': Mp3Renderer,
      'mp4': Mp4Renderer
    }
    handler = allowed_dict[self.extension()]
    return handler().render()


if __name__ == '__main__':
  f1 = FileHandler.create('test.html')
  f1.render()
