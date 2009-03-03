Name:    task-e17
Version: 2009.1
Release: %mkrel 3
Summary: Metapackage for the E17
Group:   Graphical desktop/Enlightenment
License: GPL
Epoch:	 1
URL:	 http://wiki.mandriva.com/en/Development/Ideas/E17
Source : %name.tar.bz2

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-root

# prefered apps
Suggests: exaile
Suggests: file-roller
Suggests: gimp
Suggests: thunar
Requires: %{name}-minimal
Requires: aumix
Requires: brasero
Requires: edb
Requires: elicit
Requires: emphasis
Requires: evince
Requires: expedite
Requires: gtk-chtheme
Requires: lftp
Requires: midori
Requires: mrxvt
Requires: screen
Requires: xterm
#Requires: xchat
#Requires: pidgin

%description
This package is a meta-package, meaning that its purpose is to contain
all E17 application and librairies. It also install some suggests

%package minimal
Summary: Metapackage minimal for the E17
Group:   Graphical desktop/Enlightenment
License: GPL

%description minimal
This package is a meta-package, meaning that its purpose is to contain
all E17 application and librairies.

Provides: E17
Requires: Eterm
Requires: e
Requires: eet
Requires: edje
Requires: imlib2
Requires: emotion
Requires: epsilon
Requires: etk
Requires: efreet
Requires: ewl
Requires: itask
Requires: exalt
Requires: elementary
Requires: ecore
Requires: edb
Requires: eet
Requires: embryo
Requires: estickies
Requires: esmart
Requires: e_dbus
Requires: e_modules
#Requires: epeg
#Requires: ephoto
#Requires: exhibit
#Requires: engrave
#Requires: entrance
#Requires: empower
#Requires: edje_viewer
#Requires: evfs
#Requires: extrackt
#Requires: eclair

%prep
%setup -q -n %name

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}/%{_prefix}/share/%name/doc/
cp README ${RPM_BUILD_ROOT}/%{_prefix}/share/%name/doc/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_prefix}/share/%name/doc/README

%files minimal
%defattr(-,root,root)
%{_prefix}/share/%name/doc/README
