cmake_minimum_required(VERSION 3.0)
project(TextFinder)

find_package(Qt5Widgets REQUIRED)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)

set(CMAKE_INCLUDE_CURRENT_DIR ON) # Both source and binary

add_executable(TextFinder TextFinder.cpp TextFinder.h TextFinder.ui main.cpp)

target_link_libraries(TextFinder Qt5::Widgets)
