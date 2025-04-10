# Definir la URL correcta de Python
$pythonUrl = "https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe"
$installerPath = "$env:TEMP\python-installer.exe"

# Descargar el instalador de Python
Invoke-WebRequest -Uri $pythonUrl -OutFile $installerPath

# Instalar Python en modo silencioso
Start-Process -FilePath $installerPath -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Wait

# Verificar la instalación de Python
$pythonVersion = python --version 2>$null
if ($pythonVersion) {
    Write-Host "Python se ha instalado correctamente: $pythonVersion"
} else {
    Write-Host "Error al instalar Python."
    exit 1  # Salir si hubo un error
}

# Verificar si pip está instalado
$pipVersion = python -m pip --version 2>$null
if (!$pipVersion) {
    Write-Host "pip no está instalado. Instalándolo ahora..."
    python -m ensurepip --default-pip
}

# Descargar requirements.txt desde una URL (reemplázala con la real)
$reqFileUrl = "https://tu-servidor.com/requirements.txt"
$reqFilePath = "$env:TEMP\requirements.txt"

Invoke-WebRequest -Uri $reqFileUrl -OutFile $reqFilePath

# Instalar las dependencias con pip
python -m pip install -r $reqFilePath

