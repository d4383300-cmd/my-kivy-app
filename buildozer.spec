[app]

# Название приложения на экране телефона
title = MyApp

# Внутреннее имя пакета (только английские буквы и цифры)
package.name = myapp

# Домен организации
package.domain = org.test

# Папка с исходным кодом приложения
source.dir = .

# Расширения файлов, которые попадут внутрь APK
source.include_exts = py,png,jpg,kv,atlas

# Версия вашего приложения
version = 0.1

# Зависимости проекта
requirements = python3,kivy

# Ориентация экрана: portrait, landscape или all
orientation = portrait

# Полноэкранный режим (0 - отключен, 1 - включен)
fullscreen = 0

# Разрешения Android (раскомментируйте нужные при необходимости)
# android.permissions = INTERNET,ACCESS_NETWORK_STATE

# Версии Android API и стабильный NDK
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

# Архитектуры процессоров (arm64-v8a покрывает все современные телефоны)
android.archs = arm64-v8a

[buildozer]

# Уровень вывода логов (2 = подробный вывод)
log_level = 2

# Предупреждение о запуске от root-пользователя
warn_on_root = 1
