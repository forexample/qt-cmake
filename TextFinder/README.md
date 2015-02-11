# Windows build

Prerequisites
-------------
* CMake
* Visual Studio 12 2013
* NSIS

Build
-----

`jenkins.py` python script will run next commands:
```
> cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=_install -Tv120_xp "-GVisual Studio 12 2013 Win64" -H. -B_builds
> cmake --build _builds --config Release --target install
> cd _builds
> cpack --verbose -C Release -GNSIS
```

Results:
```
> dir _install\bin\TextFinder.exe
> dir _builds\TextFinder-1.0.0-win64.exe
```

# Mac build

`jenkins.py` python script will run next commands:
```
> cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=_install -DCPACK_GENERATOR=DragNDrop -H. -B_builds -DCMAKE_MACOSX_BUNDLE=ON
> cmake --build _builds --config Release --target install
> cd _builds
> cpack --verbose -C Release -GDragNDrop
```

Results:
```
> ls _install/TextFinder.app
> ls _builds/TextFinder-1.0.0-Darwin.dmg
```
