Name:           keysmith
Version:        23.04.0
Release:        1%{?dist}
License:        GPLv3+
Summary:        Convergent OTP client
Url:            https://invent.kde.org/utilities/keysmith
Source:         https://download.kde.org/stable/plasma-mobile/%{version}/%{name}-%{version}.tar.xz
Source1:        keysmith-86.png
Source2:        keysmith-108.png
Source3:        keysmith-128.png
Source4:        keysmith-256.png

Patch0:         0001-desktop-qtrunner.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  opt-extra-cmake-modules
BuildRequires:  opt-kf5-rpm-macros
BuildRequires:  desktop-file-utils

BuildRequires:  libsodium-devel
BuildRequires:  opt-kf5-ki18n-devel
BuildRequires:  opt-kf5-kirigami2-devel
BuildRequires:  opt-kf5-kdbusaddons-devel
BuildRequires:  opt-kf5-kwindowsystem-devel
BuildRequires:  opt-qt5-qtdeclarative-devel
BuildRequires:  opt-qt5-qtsvg-devel
BuildRequires:  opt-qt5-qtquickcontrols2-devel

Requires:       opt-kf5-kirigami2
Requires:       qt-runner

%{?opt_kf5_default_filter}

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
export QTDIR=%{_opt_qt5_prefix}
touch .git

mkdir -p build
pushd build

%_opt_cmake_kf5 ../ \
		-DKDE_INSTALL_BINDIR:PATH=/usr/bin \
		-DCMAKE_INSTALL_PREFIX:PATH=/usr/
%make_build
popd

%install
pushd build
make DESTDIR=%{buildroot} install
popd

# copy icons
install -p -m644 -D %{SOURCE1} \
	%{buildroot}/%{_datadir}/icons/hicolor/86x86/apps/%{name}.png
install -p -m644 -D %{SOURCE2} \
	%{buildroot}/%{_datadir}/icons/hicolor/108x108/apps/%{name}.png
install -p -m644 -D %{SOURCE3} \
	%{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
install -p -m644 -D %{SOURCE4} \
	%{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

%check
#appstreamcli validate --no-net %{buildroot}%{_datadir}/metainfo/org.kde.%{name}.appdata.xml
#desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop

%files
%doc README.md
%license COPYING LICENSES/*.txt
%{_bindir}/%{name}
%{_datadir}/applications/org.kde.%{name}.desktop
%{_opt_kf5_metainfodir}/org.kde.%{name}.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/locale/
%{_datadir}/icons/hicolor/*/apps/%{name}.*
