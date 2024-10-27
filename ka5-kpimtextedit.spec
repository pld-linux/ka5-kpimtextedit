#
# Conditional build:
%bcond_with	tests		# test suite

%define		kdeappsver	23.08.5
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kpimtextedit
Summary:	KPIMTextedit - a textedit with PIM-specific features
Summary(pl.UTF-8):	KPIMTextedit - pole edycji tekstu z funkcjami specyficznymi dla PIM
Name:		ka5-%{kaname}
Version:	23.08.5
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	34eec446fdb47a50a6d0e3e1d3cc5668
URL:		https://kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Designer-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Speech-devel >= %{qtver}
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5UiTools-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	grantlee-qt5-devel >= 5.1
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcodecs-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kdesignerplugin-devel >= %{kframever}
BuildRequires:	kf5-kemoticons-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-ktextwidgets-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	kf5-sonnet-devel >= %{kframever}
BuildRequires:	kf5-syntax-highlighting-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
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
