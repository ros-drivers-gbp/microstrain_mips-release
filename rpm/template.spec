Name:           ros-melodic-microstrain-mips
Version:        0.0.3
Release:        1%{?dist}
Summary:        ROS microstrain_mips package

Group:          Development/Libraries
License:        GPL
URL:            http://wiki.ros.org/microstrain_3dm_gx5_45
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-cmake-modules
Requires:       ros-melodic-diagnostic-aggregator
Requires:       ros-melodic-diagnostic-updater
Requires:       ros-melodic-geometry-msgs
Requires:       ros-melodic-message-runtime
Requires:       ros-melodic-nav-msgs
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-sensor-msgs
Requires:       ros-melodic-std-msgs
Requires:       ros-melodic-std-srvs
Requires:       ros-melodic-tf2
Requires:       ros-melodic-tf2-ros
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-cmake-modules
BuildRequires:  ros-melodic-diagnostic-updater
BuildRequires:  ros-melodic-geometry-msgs
BuildRequires:  ros-melodic-message-generation
BuildRequires:  ros-melodic-nav-msgs
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-roslint
BuildRequires:  ros-melodic-sensor-msgs
BuildRequires:  ros-melodic-std-msgs
BuildRequires:  ros-melodic-std-srvs
BuildRequires:  ros-melodic-tf2
BuildRequires:  ros-melodic-tf2-ros

%description
The microstrain_mips package provides a driver for the LORD/Microstrain
3DM_GX5_XX GPS-aided IMU sensor.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Mon Aug 05 2019 Brian Bingham <briansbingham@gmail.com> - 0.0.3-1
- Autogenerated by Bloom

* Sun Aug 04 2019 Brian Bingham <briansbingham@gmail.com> - 0.0.2-2
- Autogenerated by Bloom

* Tue May 28 2019 Brian Bingham <briansbingham@gmail.com> - 0.0.2-1
- Autogenerated by Bloom

