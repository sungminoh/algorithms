# Building C++ code

This project uses cmake.

## Command line

* Prepare the build dir
    ```shell
    $ cd cpp/fact
    $ cmake -B build
    ```
* Build and run tests
    ```shell
    $ cmake --build build
    $ build/fact_test
    ```


## CLion IDE

* Open the directory you want to work in, e.g. `coding-interview/cpp` 
* Right click on `CMakeLists.txt`
* Select `Load CMake Project`
* Run/Debug targets for `fact_test` should be available
