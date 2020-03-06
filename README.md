# servis_istemci_ornek


Workspace yok ise workspace oluşturunuz.

Örn. http://wiki.ros.org/catkin/Tutorials/create_a_workspace

Daha sonra workspace gidiniz ve paketi indiriniz.

cd <WORKSPACE_NAME>

git clone "https://github.com/inomuh/servis_istemci_ornek.git"

cd <WORKSPACE_NAME>

catkin_make

catkin_make install

source devel/setup.bash




Servisi çalıştırmak için

$ rosrun servis_istemci_ornek servis_ornek_dugumu.py



İstemciyi çalıştırmak için

$ rosrun servis_istemci_ornek istemci_ornek_dugumu.py
