import serial
import io

class Interface():

    def __init__(self, port):
        self.p = port
        #self.brate = 9600
        self.brate = 1200

    def add_args(self, parser):
        parser.add_argument('--string', '-s', action="store", help='Send a string of text')


    def parse_args(self,args):

        if args.string is not None:
            self.string = args.string.replace("\\n","~:28").replace("\n","~:28").replace("~","~+54~:41~-54")

        
        self.serial = serial.Serial(self.p, self.brate, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, rtscts=0, xonxoff=1)

    def command(self, command):
        self.serial.write("~"+command)

    def send(self, data=None):
        if data is None:
            data = self.string
        self.serial.write((data+"\r").encode("utf-8"))
        self.serial.flush()


