from components.cli import Cli
from components.poweruserUI import PoweruserUI
from components.references import References
import sys

def main():
    if len(sys.argv) == 1:
        ui = Cli(References())
        ui.kaynnista()
        return
    
    PoweruserUI(References(), sys.argv)

    
    
if __name__ == "__main__":
    main()
