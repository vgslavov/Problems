cmake_minimum_required(VERSION 3.10)

macro(package_add_test TESTNAME)
    add_executable(${TESTNAME} ${ARGN})
    target_link_libraries(${TESTNAME} pthread InterviewLib)
    add_test(NAME ${TESTNAME} COMMAND ${TESTNAME})
    set_target_properties(${TESTNAME} PROPERTIES FOLDER tests)
endmacro()

file(GLOB files "./*.t.cpp")
foreach(file ${files})
    get_filename_component(file_no_ext ${file} NAME_WE)
    package_add_test(${file_no_ext} ${file})

    set_target_properties(${file_no_ext} PROPERTIES
        CXX_STANDARD 14
        CXX_STANDARD_REQUIRED YES
        CXX_EXTENSIONS NO
    )
endforeach()
