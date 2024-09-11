import os
import sys
import subprocess

def install_graphviz():
    try:
        if sys.platform.startswith('win'):
            print("Configuring Graphviz on Windows...")
            subprocess.run(['dot', '-V'], check=True)
            # Adicione o caminho do Graphviz ao PATH do PowerShell (isso é temporário para a sessão atual)
            os.environ["PATH"] += ";C:\\Program Files\\Graphviz\\bin"
        elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
            print("Configuring Graphviz on Linux or macOS...")
            subprocess.run(['dot', '-V'], check=True)
        else:
            raise OSError("Unsupported OS")
    except subprocess.CalledProcessError:
        if sys.platform.startswith('win'):
            print("Please install Graphviz from https://gitlab.com/api/v4/projects/4207231/packages/generic/graphviz-releases/12.0.0/windows_10_cmake_Release_graphviz-install-12.0.0-win64.exe and add it to your PATH.")
        elif sys.platform.startswith('linux'):
            print("Installing Graphviz on Linux...")
            if os.path.isfile('/etc/os-release'):
                with open('/etc/os-release') as f:
                    os_release = f.read()
                if 'Manjaro' in os_release:
                    subprocess.run(['sudo', 'pacman', '-S', 'graphviz'], check=True)
                else:
                    subprocess.run(['sudo', 'apt-get', 'install', 'graphviz'], check=True)
            else:
                subprocess.run(['sudo', 'apt-get', 'install', 'graphviz'], check=True)
        elif sys.platform.startswith('darwin'):
            print("Installing Graphviz on macOS...")
            subprocess.run(['brew', 'install', 'graphviz'], check=True)
        else:
            raise OSError("Unsupported OS")

    print("Graphviz configured successfully.")

def main():
    install_graphviz()

if __name__ == "__main__":
    main()
