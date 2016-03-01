import bottle

APP = bottle.default_app()

@APP.get('/')
def index():
  return '<p>Hello</p>'

if __name__ == '__main__':
  bottle.run(application=APP)
