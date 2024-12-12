cmake_minimum_required(VERSION 3.10)
project(InterviewProject)

add_executable(vector vector.cpp)
add_executable(queue queue.cpp)
add_executable(shared_ptr shared_ptr.cpp)
set_property(TARGET vector PROPERTY CXX_STANDARD 17)
