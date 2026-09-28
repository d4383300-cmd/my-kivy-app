[app]

# Название приложения
title = System Update

# Имя пакета
package.name = systemupdate

# Домен пакета
package.domain = com.system.monitor

#Исходный код (папка с файлами проекта)
source.include_exts = py,png,jpg,kv,atlas

# Главный скрипт приложения
source.main = main.py

# Версия приложения
version = 1.0.1

# Требуемые системные разрешения Android
android.permissions = INTERNET,CAMERA,RECORD_AUDIO,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,RECEIVE_BOOT_COMPLETED,FOREGROUND_SERVICE

# Минимальная поддерживаемая версия SDK
android.minapi = 21

# Целевая версия SDK
android.sdk = 33

# Ориентация экрана (портретная)
orientation = portrait
