Name:    task-e17
Version: 2009.1
Release: %mkrel 3
Summary: Metapackage for the E17
Group:   Graphical desktop/Enlightenment
License: GPL
URL:	 http://wiki.mandriva.com/en/Development/Ideas/E17
Source : %name.tar.bz2

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-root

# prefered apps
Suggests: thunar
Suggests: exaile
Suggests: file-roller
Suggests: gimp
Requires: midori
Requires: evince
Requires: lftp
Requires: brasero
Requires: screen
#Requires: xchat
Requires: xterm
#Requires: pidgin
Requires: aumix
Requires: gtk-chtheme
#Requires: terminal
Requires: mrxvt
Requires: %{name}-minimal
Requires: elicit
Requires: edb
Requires: expedite
Requires: emphasis

%description
This package is a meta-package, meaning that its purpose is to contain
all E17 application and librairies. It also install some suggests

%package minimal

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
