;------------------------------------------------------------------------------
;
;       ������ ������������� ������� ��� Inno Setup 5.5.5
;       (c) maisvendoo, 15.04.2015
;
;------------------------------------------------------------------------------

;------------------------------------------------------------------------------
;   ���������� ��������� ���������
;------------------------------------------------------------------------------

; ��� ����������
#define   Name       "SushiCalc"
; ������ ����������
#define   Version    "0.1.0"
; �����-�����������
#define   Publisher  "Djentmat"
; ���� ����� ������������
#define   URL        "https://vk.com/forsaken_horizon"
; ��� ������������ ������
#define   ExeName    "SushiCalc.exe"

;------------------------------------------------------------------------------
;   ��������� ���������
;------------------------------------------------------------------------------
[Setup]

; ���������� ������������� ����������, 
;��������������� ����� Tools -> Generate GUID
AppId={{717A0E3D-11B9-4DBD-8532-06317005B6F2}}

; ������ ����������, ������������ ��� ���������
AppName={#Name}
AppVersion={#Version}
AppPublisher={#Publisher}
AppPublisherURL={#URL}
AppSupportURL={#URL}
AppUpdatesURL={#URL}

; ���� ��������� ��-���������
DefaultDirName={pf}\{#Name}
; ��� ������ � ���� "����"
DefaultGroupName={#Name}

; �������, ���� ����� ������� ��������� setup � ��� ������������ �����
OutputDir=D:\_activity\_programming\_projects\_sushi_calc\inst
OutputBaseFileName=SushiCalcInstaller

; ���� ������
SetupIconFile=D:\_activity\_programming\_projects\_sushi_calc\Favourite2.ico

; ��������� ������
Compression=lzma
SolidCompression=yes

;------------------------------------------------------------------------------
;   ����������� - ��������� ������, ������� ���� ��������� ��� ���������
;------------------------------------------------------------------------------
[Tasks]
; �������� ������ �� ������� �����
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

;------------------------------------------------------------------------------
;   �����, ������� ���� �������� � ����� �����������
;------------------------------------------------------------------------------
[Files]

; ����������� ����
Source: "D:\_activity\_programming\_projects\_sushi_calc\dist\SushiCalc\SushiCalc.exe"; DestDir: "{app}"; Flags: ignoreversion

; ������������� �������
Source: "D:\_activity\_programming\_projects\_sushi_calc\dist\SushiCalc\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

;------------------------------------------------------------------------------
;   ��������� �����������, ��� �� ������ ����� ������
;------------------------------------------------------------------------------ 
[Icons]

Name: "{group}\{#Name}"; Filename: "{app}\{#ExeName}"

Name: "{commondesktop}\{#Name}"; Filename: "{app}\{#ExeName}"; Tasks: desktopicon