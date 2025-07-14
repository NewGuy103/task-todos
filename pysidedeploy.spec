[app]

# title of your application
title = task-todos

# project root directory. default = The parent directory of input_file
project_dir = .

# source file entry point path. default = main.py
input_file = main.py

# directory where the executable output is generated
exec_directory = dist_out

# path to the project file relative to project_dir
project_file = 

# application icon
icon = 

[python]

# python path
python_path = .venv/bin/python3

# python packages to install
# already handled by uv for the base dependencies
packages = Nuitka==2.6.8

# buildozer = for deploying Android application
android_packages = buildozer==1.5.0,cython==0.29.33

[qt]

# paths to required qml files. comma separated
# normally all the qml files required by the project are added automatically
qml_files = 

# excluded qml plugin binaries
excluded_qml_plugins = 

# qt modules used. comma separated
modules = Gui,Core,DBus,Widgets

# qt plugins used by the application. only relevant for desktop deployment
# for qt plugins used in android application see [android][plugins]
plugins = egldeviceintegrations,platforms,accessiblebridge,imageformats,platforms/darwin,platforminputcontexts,xcbglintegrations,generic,styles,iconengines,platformthemes

[android]

# path to pyside wheel
wheel_pyside = pyside6-wheels/PySide6-6.9.1-6.9.1-cp311-cp311-android_aarch64.whl

# path to shiboken wheel
wheel_shiboken = pyside6-wheels/shiboken6-6.9.1-6.9.1-cp311-cp311-android_aarch64.whl

# plugins to be copied to libs folder of the packaged application. comma separated
plugins = platforms_qtforandroid

[nuitka]

# usage description for permissions requested by the app as found in the info.plist file
# of the app bundle. comma separated
# eg = extra_args = --show-modules --follow-stdlib
macos.permissions = 

# mode of using nuitka. accepts standalone or onefile. default = onefile
mode = onefile

# specify any extra nuitka arguments
extra_args = --quiet --noinclude-qt-translations --assume-yes-for-downloads

[buildozer]

# build mode
# possible values = ["aarch64", "armv7a", "i686", "x86_64"]
# release creates a .aab, while debug creates a .apk
mode = debug

# path to pyside6 and shiboken6 recipe dir
recipe_dir = deployment/recipes

# path to extra qt android .jar files to be loaded by the application
jars_dir = deployment/jar/PySide6/jar

# if empty, uses default ndk path downloaded by buildozer
ndk_path = ~/.pyside6_android_deploy/android-ndk/android-ndk-r27c

# if empty, uses default sdk path downloaded by buildozer
sdk_path = ~/.pyside6_android_deploy/android-sdk

# other libraries to be loaded at app startup. comma separated.
local_libs = plugins_platforms_qtforandroid

# architecture of deployed platform
arch = arm64-v8a

