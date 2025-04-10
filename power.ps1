# Verificar si Python está instalado
$pythonPath = Get-Command python -ErrorAction SilentlyContinue

if ($pythonPath) {
    Write-Host "Python ya está instalado: $($pythonPath.Source)"
} else {
    Write-Host "Python no está instalado. Iniciando la descarga e instalación..."

    # Definir la URL correcta de Python
    $pythonUrl = "https://www.python.org/ftp/python/3.13.2/python-3.13.2-amd64.exe"
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
}

# Descargar el archivo requirements.txt desde una URL
$reqFileUrl = "https://raw.githubusercontent.com/DankNetherite/OdooPython/refs/heads/main/librerias.txt"
$reqFilePath = "$env:TEMP\requirements.txt"

Invoke-WebRequest -Uri $reqFileUrl -OutFile $reqFilePath

# Instalar las dependencias con pip
Write-Host "Instalando dependencias desde $reqFilePath..."
python -m pip install -r $reqFilePath

# Ejecutar el script Python directamente desde la URL utilizando Invoke-RestMethod (irm)
Write-Host "Ejecutando el script Python desde la URL..."

irm https://raw.githubusercontent.com/DankNetherite/OdooPython/refs/heads/main/erp.py | py
