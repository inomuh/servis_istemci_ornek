cmake_minimum_required(VERSION 2.8.3)
project(servis_istemci_ornek)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_srvs
  message_generation
)

 generate_messages(
   DEPENDENCIES
   std_srvs
 )

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

foreach(dir launch scripts)
    install(DIRECTORY ${dir}/
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach()