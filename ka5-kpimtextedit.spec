#
# Conditional build:
%bcond_with	tests		# test suite

%define		kdeappsver	%{version}
%define		kf_ver		5.105.0
%define		qt_ver		5.15.2
%define		kaname		kpimtextedit
Summary:	KPIMTextedit - a textedit with PIM-specific features
Summary(pl.UTF-8):	KPIMTextedit - pole edycji tekstu z funkcjami specyficznymi dla PIM
Name:		ka5-%{kaname}
Version:	23.08.5
Release:	2
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	34eec446fdb47a50a6d0e3e1d3cc5668
URL:		https://kde.org/
BuildRequires:	Qt5Core-devel >= %{qt_ver}
BuildRequires:	Qt5Designer-devel >= %{qt_ver}
BuildRequires:	Qt5Gui-devel >= %{qt_ver}
%if %{with tests}
BuildRequires:	Qt5Test-devel >= %{qt_ver}
%endif
BuildRequires:	Qt5UiTools-devel >= %{qt_ver}
BuildRequires:	Qt5Widgets-devel >= %{qt_ver}
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-tools
BuildRequires:	kf5-extra-cmake-modules >= %{kf_ver}
BuildRequires:	kf5-kcodecs-devel >= %{kf_ver}
BuildRequires:	kf5-kconfig-devel >= %{kf_ver}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kf_ver}
BuildRequires:	kf5-kcoreaddons-devel >= %{kf_ver}
BuildRequires:	kf5-ki18n-devel >= %{kf_ver}
BuildRequires:	kf5-kiconthemes-devel >= %{kf_ver}
BuildRequires:	kf5-kio-devel >= %{kf_ver}
BuildRequires:	kf5-ktextaddons-devel >= 1.0.0
%if %{with tests}
BuildRequires:	kf5-ktextwidgets-devel >= %{kf_ver}
%endif
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kf_ver}
BuildRequires:	kf5-kxmlgui-devel >= %{kf_ver}
BuildRequires:	kf5-sonnet-devel >= %{kf_ver}
BuildRequires:	kf5-syntax-highlighting-devel >= %{kf_ver}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	Qt5Core >= %{qt_ver}
Requires:	Qt5Gui >= %{qt_ver}
Requires:	Qt5Widgets >= %{qt_ver}
Requires:	kf5-kcodecs >= %{kf_ver}
Requires:	kf5-kconfig >= %{kf_ver}
Requires:	kf5-kconfigwidgets >= %{kf_ver}
Requires:	kf5-kcoreaddons >= %{kf_ver}
Requires:	kf5-ki18n >= %{kf_ver}
Requires:	kf5-kio >= %{kf_ver}
Requires:	kf5-ktextaddons >= 1.0.0
Requires:	kf5-kwidgetsaddons >= %{kf_ver}
Requires:	kf5-kxmlgui >= %{kf_ver}
Requires:	kf5-sonnet >= %{kf_ver}
Requires:	kf5-syntax-highlighting >= %{kf_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KPIMTextedit provides a textedit with PIM-specific features.

%description -l pl.UTF-8
KPIMTextedit dostarcza pole edycji tekstu z funkcjami specyficznymi
dla PIM.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kf5-ktextwidgets-devel >= 5.105.0
Requires:	kf5-ktextaddons-devel >= 1.0.0

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_SYSCONFDIR=%{_sysconfdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang libkpimtextedit

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f libkpimtextedit.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libKPim5TextEdit.so.*.*.*
%ghost %{_libdir}/libKPim5TextEdit.so.5
%{_datadir}/qlogging-categories5/kpimtextedit.categories
%{_libdir}/qt5/plugins/designer/kpimtextedit5widgets.so

%files devel
%defattr(644,root,root,755)
%{_libdir}/libKPim5TextEdit.so
%{_includedir}/KPim5/KPIMTextEdit
%{_libdir}/cmake/KF5PimTextEdit
%{_libdir}/cmake/KPim5TextEdit
%{_libdir}/qt5/mkspecs/modules/qt_KPIMTextEdit.pri
