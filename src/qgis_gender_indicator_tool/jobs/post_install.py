import subprocess
import sys
import shutil
from qgis.core import QgsMessageLog, Qgis

def check_pip_installed():
    if shutil.which('pip') is None:
        QgsMessageLog.logMessage(
            "pip is not installed. Please install pip before installing the GEEST plugin.\n"
            "You can install pip by following the instructions at https://pip.pypa.io/en/stable/installation/",
            'GEEST',
            level=Qgis.Critical
        )
        sys.exit(1)

def install_requirements():
    try:
        QgsMessageLog.logMessage("Installing requirements...", 'GEEST', level=Qgis.Info)
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        QgsMessageLog.logMessage("Requirements installed successfully.", 'GEEST', level=Qgis.Success)
    except subprocess.CalledProcessError as e:
        QgsMessageLog.logMessage(f"Failed to install requirements: {e}", 'GEEST', level=Qgis.Critical)
        sys.exit(1)

if __name__ == '__main__':
    check_pip_installed()
    install_requirements()
