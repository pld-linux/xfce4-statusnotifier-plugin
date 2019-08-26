Summary:	A panel area for status notifier items (application indicators)
Name:		xfce4-statusnotifier-plugin
Version:	0.2.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-statusnotifier-plugin/0.2/%{name}-%{version}.tar.bz2
# Source0-md5:	152a327049e3977c439961d3e007e14d
URL:		https://goodies.xfce.org/projects/panel-plugins/xfce4-statusnotifier-plugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.30.2
BuildRequires:	gtk+3-devel
BuildRequires:	intltool
BuildRequires:	libdbusmenu-gtk3-devel
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel >= 4.14.0
BuildRequires:	libxfce4util-devel >= 4.14.0
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.14.0
BuildRequires:	xfce4-panel-devel >= 4.14.0
Requires:	xfce4-panel >= 4.14.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin provides a panel area for status notifier items
(application indicators). Applications may use these items to display
their status and interact with user. This technology is a modern
alternative to systray and has the freedesktop.org specification.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xfce4/panel/plugins/libstatusnotifier.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libstatusnotifier.so
%{_datadir}/xfce4/panel/plugins/statusnotifier.desktop
%{_iconsdir}/hicolor/*x*/apps/xfce4-statusnotifier-plugin.png
%{_iconsdir}/hicolor/scalable/apps/xfce4-statusnotifier-plugin.svg
