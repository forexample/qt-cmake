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

if(CMAKE_MACOSX_BUNDLE)
  install(
      DIRECTORY "${Qt5Widgets_DIR}/../../../plugins/platforms"
      DESTINATION "TextFinder.app/Contents/MacOS"
  )

  set(gen "${CMAKE_CURRENT_BINARY_DIR}/fixup.cmake")
  configure_file("cmake/fixup.cmake.in" "${gen}" @ONLY)
  install(SCRIPT "${gen}")
endif()

include("cmake/pack.cmake")
