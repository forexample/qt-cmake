cmake_minimum_required(VERSION 3.0)
project(TextFinder VERSION 1.0.0)

find_package(Qt5Widgets REQUIRED)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTORCC ON)

set(CMAKE_INCLUDE_CURRENT_DIR ON) # Both source and binary

add_executable(
    TextFinder
    TextFinder.cpp
    TextFinder.h
    TextFinder.ui
    TextFinder.qrc
    main.cpp
    input.txt
)

target_link_libraries(TextFinder Qt5::Widgets)

install(
    TARGETS TextFinder
    BUNDLE DESTINATION .
    RUNTIME DESTINATION bin
)

set(CMAKE_INSTALL_DEBUG_LIBRARIES YES)
include(InstallRequiredSystemLibraries)

if(CMAKE_MACOSX_BUNDLE)
  set(platform_dest "TextFinder.app/Contents/MacOS")
else()
  set(platform_dest bin)
endif()

if(APPLE OR WIN32)
  install(
      DIRECTORY "${Qt5Widgets_DIR}/../../../plugins/platforms"
      DESTINATION ${platform_dest}
  )
endif()

if(MSVC)
  # Install libraries manually (workaround for cpack)
  # See: http://public.kitware.com/Bug/view.php?id=15400

  get_filename_component(qt_root "${Qt5Widgets_DIR}/../../../" ABSOLUTE)

  # Qt deps
  foreach(qtdep icuin53 icuuc53 icudt53)
    set(qtdep_location "${qt_root}/bin/${qtdep}.dll")
    if(NOT EXISTS "${qtdep_location}")
      message(FATAL_ERROR "Not found: ${qtdep_location}")
    endif()
    install(FILES "${qtdep_location}" DESTINATION bin)
  endforeach()

  # Qt libs
  foreach(qtlib Qt5Widgets Qt5Gui Qt5Core)
    set(qtlib_release "${qt_root}/bin/${qtlib}.dll")
    set(qtlib_debug "${qt_root}/bin/${qtlib}d.dll")
    if(NOT EXISTS "${qtlib_release}")
      message(FATAL_ERROR "Not found: ${qtlib_release}")
    endif()
    if(NOT EXISTS "${qtlib_debug}")
      message(FATAL_ERROR "Not found: ${qtlib_debug}")
    endif()
    install(FILES "${qtlib_release}" DESTINATION bin CONFIGURATIONS Release)
    install(FILES "${qtlib_debug}" DESTINATION bin CONFIGURATIONS Debug)
  endforeach()
endif()

if(APPLE OR WIN32)
  set(gen "${CMAKE_CURRENT_BINARY_DIR}/fixup.cmake")
  configure_file("cmake/fixup.cmake.in" "${gen}" @ONLY)
  install(SCRIPT "${gen}")
endif()

include("cmake/pack.cmake")
