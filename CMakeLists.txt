cmake_minimum_required(VERSION 3.0)

include("gate/cmake/HunterGate.cmake")
HunterGate(
    URL "https://github.com/ingenue/hunter/archive/experimental-0.tar.gz"
    SHA1 "ab3991e1bb5ccb68ef52975094dee2be2cc875a0"
)

project(QtCMakeExamples)

add_subdirectory(TextFinder)
