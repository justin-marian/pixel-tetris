import os
import sys
import subprocess


def install(package):
    """
    Install a Python package using pip.

    Args:
        package (str): The name of the package to install.

    Returns:
        None
    """
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def install_dependencies():
    """
    Install required Python packages if not already installed.

    This function checks if the required packages (pygame, colorama, requests) are installed.
    If any of them are missing, it installs them using the `install` function.

    Returns:
        None
    """
    required = ["pygame", "colorama", "requests"]
    for package in required:
        try:
            __import__(package)
        except ImportError:
            print(f"Installing missing package: {package}")
            install(package)

def run_tetris():
    """
    Run the Tetris game script.

    This function attempts to run the Tetris game script (Tetris.py) using the Python interpreter.
    It checks if the script exists in the same directory as this script and runs it.

    Returns:
        None
    """
    try:
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        tetris_path = os.path.join(script_dir, 'Tetris.py')

        subprocess.run([sys.executable, tetris_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while trying to run Tetris.py: {e}")

def print_tetris_ascii():
    """
    Print the word 'TETRIS' in ASCII art with colored text.

    This function uses the colorama library to print the word 'TETRIS' in ASCII art with colored text.
    It initializes colorama, sets text colors, and prints the art to the console.

    Returns:
        None
    """
    from colorama import Fore, init
    init()
    print(f"{Fore.BLACK}╔████══███═══███══███████══█████████══█████████══███████═══████══██████╗{Fore.RESET}")
    print(f"{Fore.BLACK}║████══███                                                 ████══██████║{Fore.RESET}")
    print(f"{Fore.RED}             ████████╗███████╗████████╗█████╗  ██╗███████╗                   {Fore.RESET}")
    print(f"{Fore.YELLOW}             ╚══██╔══╝██╔════╝╚══██╔══╝██╔══██╗██║██╔════╝                {Fore.RESET}")
    print(f"{Fore.GREEN}                ██║   █████╗     ██║   ███████║██║███████╗                 {Fore.RESET}")
    print(f"{Fore.BLUE}                ██║   ██╔══╝     ██║   ██║██║  ██║╚════██║                  {Fore.RESET}")
    print(f"{Fore.MAGENTA}                ██║   ███████╗   ██║   ██║  ██║██║███████║               {Fore.RESET}")
    print(f"{Fore.CYAN}                ╚═╝   ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝                  {Fore.RESET}")
    print(f"{Fore.BLACK}║████══███                                                 ████══██████║{Fore.RESET}")
    print(f"{Fore.BLACK}╚████══███═══███══███████══█████████══█████████══███████═══████══██████╝{Fore.RESET}")

if __name__ == '__main__':
    install_dependencies()
    print_tetris_ascii()
    run_tetris()
