# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "grp6_proj: 2 messages, 0 services")

set(MSG_I_FLAGS "-Igrp6_proj:/home/ros/catkin_ws/src/grp6_proj/msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(grp6_proj_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/ros/catkin_ws/src/grp6_proj/msg/block_coords.msg" NAME_WE)
add_custom_target(_grp6_proj_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "grp6_proj" "/home/ros/catkin_ws/src/grp6_proj/msg/block_coords.msg" ""
)

get_filename_component(_filename "/home/ros/catkin_ws/src/grp6_proj/msg/block_coords_array.msg" NAME_WE)
add_custom_target(_grp6_proj_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "grp6_proj" "/home/ros/catkin_ws/src/grp6_proj/msg/block_coords_array.msg" "grp6_proj/block_coords"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(grp6_proj
  "/home/ros/catkin_ws/src/grp6_proj/msg/block_coords.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/grp6_proj
)
_generate_msg_cpp(grp6_proj
  "/home/ros/catkin_ws/src/grp6_proj/msg/block_coords_array.msg"
  "${MSG_I_FLAGS}"
  "/home/ros/catkin_ws/src/grp6_proj/msg/block_coords.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/grp6_proj
)

### Generating Services

### Generating Module File
_generate_module_cpp(grp6_proj
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/grp6_proj
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(grp6_proj_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(grp6_proj_generate_messages grp6_proj_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ros/catkin_ws/src/grp6_proj/msg/block_coords.msg" NAME_WE)
add_dependencies(grp6_proj_generate_messages_cpp _grp6_proj_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ros/catkin_ws/src/grp6_proj/msg/block_coords_array.msg" NAME_WE)
add_dependencies(grp6_proj_generate_messages_cpp _grp6_proj_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(grp6_proj_gencpp)
add_dependencies(grp6_proj_gencpp grp6_proj_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS grp6_proj_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(grp6_proj
  "/home/ros/catkin_ws/src/grp6_proj/msg/block_coords.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/grp6_proj
)
_generate_msg_eus(grp6_proj
  "/home/ros/catkin_ws/src/grp6_proj/msg/block_coords_array.msg"
  "${MSG_I_FLAGS}"
  "/home/ros/catkin_ws/src/grp6_proj/msg/block_coords.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/grp6_proj
)

### Generating Services

### Generating Module File
_generate_module_eus(grp6_proj
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/grp6_proj
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(grp6_proj_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(grp6_proj_generate_messages grp6_proj_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ros/catkin_ws/src/grp6_proj/msg/block_coords.msg" NAME_WE)
add_dependencies(grp6_proj_generate_messages_eus _grp6_proj_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ros/catkin_ws/src/grp6_proj/msg/block_coords_array.msg" NAME_WE)
add_dependencies(grp6_proj_generate_messages_eus _grp6_proj_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(grp6_proj_geneus)
add_dependencies(grp6_proj_geneus grp6_proj_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS grp6_proj_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(grp6_proj
  "/home/ros/catkin_ws/src/grp6_proj/msg/block_coords.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/grp6_proj
)
_generate_msg_lisp(grp6_proj
  "/home/ros/catkin_ws/src/grp6_proj/msg/block_coords_array.msg"
  "${MSG_I_FLAGS}"
  "/home/ros/catkin_ws/src/grp6_proj/msg/block_coords.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/grp6_proj
)

### Generating Services

### Generating Module File
_generate_module_lisp(grp6_proj
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/grp6_proj
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(grp6_proj_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(grp6_proj_generate_messages grp6_proj_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ros/catkin_ws/src/grp6_proj/msg/block_coords.msg" NAME_WE)
add_dependencies(grp6_proj_generate_messages_lisp _grp6_proj_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ros/catkin_ws/src/grp6_proj/msg/block_coords_array.msg" NAME_WE)
add_dependencies(grp6_proj_generate_messages_lisp _grp6_proj_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(grp6_proj_genlisp)
add_dependencies(grp6_proj_genlisp grp6_proj_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS grp6_proj_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(grp6_proj
  "/home/ros/catkin_ws/src/grp6_proj/msg/block_coords.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/grp6_proj
)
_generate_msg_nodejs(grp6_proj
  "/home/ros/catkin_ws/src/grp6_proj/msg/block_coords_array.msg"
  "${MSG_I_FLAGS}"
  "/home/ros/catkin_ws/src/grp6_proj/msg/block_coords.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/grp6_proj
)

### Generating Services

### Generating Module File
_generate_module_nodejs(grp6_proj
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/grp6_proj
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(grp6_proj_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(grp6_proj_generate_messages grp6_proj_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ros/catkin_ws/src/grp6_proj/msg/block_coords.msg" NAME_WE)
add_dependencies(grp6_proj_generate_messages_nodejs _grp6_proj_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ros/catkin_ws/src/grp6_proj/msg/block_coords_array.msg" NAME_WE)
add_dependencies(grp6_proj_generate_messages_nodejs _grp6_proj_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(grp6_proj_gennodejs)
add_dependencies(grp6_proj_gennodejs grp6_proj_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS grp6_proj_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(grp6_proj
  "/home/ros/catkin_ws/src/grp6_proj/msg/block_coords.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/grp6_proj
)
_generate_msg_py(grp6_proj
  "/home/ros/catkin_ws/src/grp6_proj/msg/block_coords_array.msg"
  "${MSG_I_FLAGS}"
  "/home/ros/catkin_ws/src/grp6_proj/msg/block_coords.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/grp6_proj
)

### Generating Services

### Generating Module File
_generate_module_py(grp6_proj
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/grp6_proj
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(grp6_proj_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(grp6_proj_generate_messages grp6_proj_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ros/catkin_ws/src/grp6_proj/msg/block_coords.msg" NAME_WE)
add_dependencies(grp6_proj_generate_messages_py _grp6_proj_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ros/catkin_ws/src/grp6_proj/msg/block_coords_array.msg" NAME_WE)
add_dependencies(grp6_proj_generate_messages_py _grp6_proj_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(grp6_proj_genpy)
add_dependencies(grp6_proj_genpy grp6_proj_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS grp6_proj_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/grp6_proj)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/grp6_proj
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(grp6_proj_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/grp6_proj)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/grp6_proj
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(grp6_proj_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/grp6_proj)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/grp6_proj
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(grp6_proj_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/grp6_proj)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/grp6_proj
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(grp6_proj_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/grp6_proj)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/grp6_proj\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/grp6_proj
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(grp6_proj_generate_messages_py std_msgs_generate_messages_py)
endif()
