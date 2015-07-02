class Lines:
  def __init__(self, f):
    self.path = f
    self.d = []
    self.compile()

  def compile(self):
    offset = 0
    with open(self.path, 'r') as f:
      for line in f:
        self.d.append(offset)
        offset += len(line)

  def find_line(self, n):
    offset = self.d[n]

    line = ''
    with open(self.path, 'r') as f:
      f.seek(offset)
      line = f.readline().strip()
    return line

def main():
  l = Lines(f='/usr/share/dict/words')
  for n in xrange(len(l.d)):
    print n, l.find_line(n=n)

if __name__ == '__main__':
  main()