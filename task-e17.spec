Name:    task-e17
Version: 2008
Release: %mkrel 1
Summary: Metapackage for the E17
Group:   Graphical desktop/Enlightenment
License: GPL

Source : %name.tar.bz2

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-root

Provides: E17

# prefered apps
Requires: thunar
Requires: rhythmbox
Requires: firefox
Requires: evince
Requires: lftp
Requires: brasero
Requires: gimp
Requires: screen
#Requires: xchat
Requires: xterm
#Requires: pidgin
Requires: aumix

# E17 apps
Requires: e
Requires: eet
Requires: e_utils
Requires: enity
Requires: edje
Requires: imlib2
Requires: emotion
Requires: epsilon
Requires: etk
Requires: efreet
Requires: ewl
Requires: epeg
Requires: ecore
Requires: evas
Requires: edb
Requires: eet
Requires: embryo
Requires: ephoto
Requires: exhibit
Requires: engrave
Requires: enhance
Requires: entrance
Requires: estickies
Requires: empower
Requires: edje_viewer
Requires: e_modules

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running the E17 Mandriva Desktop.

%prep

%install
rm -rf $RPM_BUILD_ROOT

%post

%files
