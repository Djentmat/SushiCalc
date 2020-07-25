;------------------------------------------------------------------------------
;
;       Пример установочного скрипта для Inno Setup 5.5.5
;       (c) maisvendoo, 15.04.2015
;
;------------------------------------------------------------------------------

;------------------------------------------------------------------------------
;   Определяем некоторые константы
;------------------------------------------------------------------------------

; Имя приложения
#define   Name       "SushiCalc"
; Версия приложения
#define   Version    "0.1.0"
; Фирма-разработчик
#define   Publisher  "Djentmat"
; Сафт фирмы разработчика
#define   URL        "https://vk.com/forsaken_horizon"
; Имя исполняемого модуля
#define   ExeName    "SushiCalc.exe"

;------------------------------------------------------------------------------
;   Параметры установки
;------------------------------------------------------------------------------
[Setup]

; Уникальный идентификатор приложения, 
;сгенерированный через Tools -> Generate GUID
AppId={{717A0E3D-11B9-4DBD-8532-06317005B6F2}}

; Прочая информация, отображаемая при установке
AppName={#Name}
AppVersion={#Version}
AppPublisher={#Publisher}
AppPublisherURL={#URL}
AppSupportURL={#URL}
AppUpdatesURL={#URL}

; Путь установки по-умолчанию
DefaultDirName={pf}\{#Name}
; Имя группы в меню "Пуск"
DefaultGroupName={#Name}

; Каталог, куда будет записан собранный setup и имя исполняемого файла
OutputDir=D:\_activity\_programming\_projects\_sushi_calc\inst
OutputBaseFileName=SushiCalcInstaller

; Файл иконки
SetupIconFile=D:\_activity\_programming\_projects\_sushi_calc\Favourite2.ico

; Параметры сжатия
Compression=lzma
SolidCompression=yes

;------------------------------------------------------------------------------
;   Опционально - некоторые задачи, которые надо выполнить при установке
;------------------------------------------------------------------------------
[Tasks]
; Создание иконки на рабочем столе
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

;------------------------------------------------------------------------------
;   Файлы, которые надо включить в пакет установщика
;------------------------------------------------------------------------------
[Files]

; Исполняемый файл
Source: "D:\_activity\_programming\_projects\_sushi_calc\dist\SushiCalc\SushiCalc.exe"; DestDir: "{app}"; Flags: ignoreversion

; Прилагающиеся ресурсы
Source: "D:\_activity\_programming\_projects\_sushi_calc\dist\SushiCalc\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

;------------------------------------------------------------------------------
;   Указываем установщику, где он должен взять иконки
;------------------------------------------------------------------------------ 
[Icons]

Name: "{group}\{#Name}"; Filename: "{app}\{#ExeName}"

Name: "{commondesktop}\{#Name}"; Filename: "{app}\{#ExeName}"; Tasks: desktopicon