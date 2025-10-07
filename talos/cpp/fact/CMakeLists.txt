cmake_minimum_required(VERSION 3.21)
project(fact)

set(CMAKE_CXX_STANDARD 20)

include(FetchContent)
FetchContent_Declare(
        googletest
        URL https://github.com/google/googletest/archive/e2239ee6043f73722e7aa812a459f54a28552929.zip
)

# For Windows: Prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

add_library(fact fact.cpp)
add_executable(fact_test fact_test.cpp)
target_link_libraries(fact_test fact gtest_main)

include(GoogleTest)
gtest_discover_tests(fact_test)
