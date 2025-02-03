; Datos del ejecutable y la aplicacion
OutFile "actividad3.exe"
Name "Gestor Reservas"
Icon "hotel.ico"

; Carpeta por defecto
InstallDir "$PROGRAMFILES\hotel"

; Páginas del instalador
Page directory
Page license
LicenseData "LICENSE.txt"  
Page instfiles

; Seccion de instalacion
Section "Install"

    ; Directorio destino
    SetOutPath "$INSTDIR"

    ; Acceso directo
    CreateShortCut "$DESKTOP\Gestor Reservas.lnk" "$INSTDIR\actividad2.exe" "" "$INSTDIR\hotel.ico"

    ; Copiar los archivos necesarios a la carpeta de instalacion
    File "actividad2.exe"
    File "hotel.ico"

    ; Registra la aplicacion en el registro de Windows para la desinstalacion
    WriteRegStr HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\GestorReservas" "UninstallString" "$INSTDIR\uninstall.exe"
    WriteRegStr HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\GestorReservas" "InstallLocation" "$INSTDIR"
    WriteRegStr HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\GestorReservas" "DisplayName" "Gestor Reservas"

    ; Añadir el desinstalador en el directorio de instalacion
    WriteUninstaller "$INSTDIR\uninstall.exe"

SectionEnd

; Iniciar las páginas del desinstalador
UninstPage uninstConfirm
UninstPage instfiles

; Seccion de desinstalacion
Section "Uninstall"

    ; Eliminar el acceso directo del escritorio
    Delete "$DESKTOP\Gestor Reservas.lnk"

    ; Eliminar los archivos generados y el directorio
    Delete "$INSTDIR\actividad2.exe"
    Delete "$INSTDIR\hotel.ico"
    Delete "$INSTDIR\uninstall.exe"
    RMDir $INSTDIR

    ; Eliminar la clave del registro de la aplicacion
    DeleteRegKey HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\GestorReservas"
    
SectionEnd

