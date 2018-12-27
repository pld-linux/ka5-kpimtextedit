%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		kpimtextedit
Summary:	kpimtextedit
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	e8ce44e80d4022f94fd852ce9bb10315
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Designer-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Speech-devel >= %{qtver}
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5UiTools-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	grantlee-qt5-devel >= 5.1
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kcodecs-devel >= 5.51.0
BuildRequires:	kf5-kconfig-devel >= 5.51.0
BuildRequires:	kf5-kconfigwidgets-devel >= 5.51.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.51.0
BuildRequires:	kf5-kemoticons-devel >= 5.51.0
BuildRequires:	kf5-ki18n-devel >= 5.51.0
BuildRequires:	kf5-kiconthemes-devel >= 5.51.0
BuildRequires:	kf5-kio-devel >= 5.51.0
BuildRequires:	kf5-ktextwidgets-devel >= 5.51.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.51.0
BuildRequires:	kf5-kxmlgui-devel >= 5.51.0
BuildRequires:	kf5-sonnet-devel >= 5.51.0
BuildRequires:	kf5-syntax-highlighting-devel >= 5.51.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kpimtextedit.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/kpimtextedit.categories
%attr(755,root,root) %ghost %{_libdir}/libKF5PimTextEdit.so.5
%attr(755,root,root) %{_libdir}/libKF5PimTextEdit.so.5.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/designer/kpimtexteditwidgets.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KPIMTextEdit
%{_includedir}/KF5/kpimtextedit_version.h
%{_libdir}/cmake/KF5PimTextEdit
%attr(755,root,root) %{_libdir}/libKF5PimTextEdit.so
%{_libdir}/qt5/mkspecs/modules/qt_KPIMTextEdit.pri
