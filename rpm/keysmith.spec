Name:           keysmith
Version:        26.04.3
Release:        1%{?dist}
License:        GPLv3+
Summary:        Convergent OTP client
Url:            https://invent.kde.org/utilities/keysmith
Source:         https://download.kde.org/stable/plasma-mobile/%{version}/%{name}-%{version}.tar.xz
Source1:        keysmith-86.png
Source2:        keysmith-108.png
Source3:        keysmith-128.png
Source4:        keysmith-256.png

Patch0:         0000-build-for-sailfishos.patch
Patch1:         0001-desktop-qt6-start.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  desktop-file-utils

BuildRequires:  libsodium-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kirigami-devel
BuildRequires:  kf6-kirigami-addons-devel
BuildRequires:  kf6-kdbusaddons-devel
#BuildRequires:  kf6-kwindowsystem-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  kf6-kconfig-devel
BuildRequires:  kf6-prison-devel

# this is just required because we piggy-back on the Android build spec
BuildRequires:  pkgconfig(openssl)

Requires:       kf6-kirigami
Requires:       qt-runner-qt6

%description
OTP client for Plasma Mobile and Desktop
%if 0%{?_chum}
PackageName: Keysmith
Type: desktop-application
DeveloperName: KDE Project
PackagerName: Adam Pigg
Categories:
 - Utility
Custom:
  Repo: https://invent.kde.org/utilities/keysmith
  PackagingRepo: https://github.com/sailfishos-chum/keysmith
Icon: https://raw.githubusercontent.com/sailfishos-chum/keysmith/main/rpm/keysmith-128.png
Screenshots:
 - https://github.com/sailfishos-chum/keysmith/raw/main/screenshot-1.png
 - https://github.com/sailfishos-chum/keysmith/raw/main/screenshot-2.png
%endif

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
%cmake_kf6 \
        -DSAILFISHOS=ON \
        -DKDE_INSTALL_BINDIR:PATH=/usr/bin \
        -DCMAKE_INSTALL_PREFIX:PATH=/usr/
%cmake_build

%install
%cmake_install

# copy icons
install -p -m644 -D %{SOURCE1} \
    %{buildroot}/%{_datadir}/icons/hicolor/86x86/apps/org.kde.%{name}.png
install -p -m644 -D %{SOURCE2} \
    %{buildroot}/%{_datadir}/icons/hicolor/108x108/apps/org.kde.%{name}.png
install -p -m644 -D %{SOURCE3} \
    %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/org.kde.%{name}.png
install -p -m644 -D %{SOURCE4} \
    %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/org.kde.%{name}.png

%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%license COPYING LICENSES/*.txt
%{_bindir}/%{name}
%{_datadir}/applications/org.kde.%{name}.desktop
%exclude %{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/org.kde.%{name}.svg
%{_datadir}/icons/hicolor/*/apps/org.kde.%{name}.*
