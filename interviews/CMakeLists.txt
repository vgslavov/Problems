cmake_minimum_required(VERSION 3.10)
project(InterviewProject)

add_executable(vector vector.cpp)
set_property(TARGET vector PROPERTY CXX_STANDARD 17)

add_executable(vector2 vector2.cpp)
set_property(TARGET vector2 PROPERTY CXX_STANDARD 17)

add_executable(queue queue.cpp)
set_property(TARGET queue PROPERTY CXX_STANDARD 17)

add_executable(queue2 queue2.cpp)
set_property(TARGET queue2 PROPERTY CXX_STANDARD 17)

add_executable(shared_ptr shared_ptr.cpp)
set_property(TARGET shared_ptr PROPERTY CXX_STANDARD 17)

add_executable(unique_ptr unique_ptr.cpp)
set_property(TARGET unique_ptr PROPERTY CXX_STANDARD 17)

add_executable(rule_of_three rule_of_three.cpp)
set_property(TARGET rule_of_three PROPERTY CXX_STANDARD 17)

add_executable(rule_of_five rule_of_five.cpp)
set_property(TARGET rule_of_five PROPERTY CXX_STANDARD 17)

add_executable(rule_of_zero rule_of_zero.cpp)
set_property(TARGET rule_of_zero PROPERTY CXX_STANDARD 17)

add_executable(copy_swap copy_swap.cpp)
set_property(TARGET copy_swap PROPERTY CXX_STANDARD 17)
