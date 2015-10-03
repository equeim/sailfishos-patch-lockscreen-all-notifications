Name: sailfishos-patch-lockscreen-all-notifications
BuildArch: noarch
Summary: Show all notifications on lockscreen
Version: 0.1
Release: 1
Group: System/Patches
License: GPLv3
URL: https://github.com/equeim/sailfishos-patch-lockscreen-all-notifications
Source0: %{name}-%{version}.tar.xz
Requires: patchmanager
Requires: sailfish-version >= 1.1.9

%description
Show all notifications on lockscreen

%prep
%setup -q -n %{name}-%{version}


%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/share/patchmanager/patches/sailfishos-patch-lockscreen-all-notifications
cp -r patch/* %{buildroot}/usr/share/patchmanager/patches/sailfishos-patch-lockscreen-all-notifications

%pre
if [ -d /var/lib/patchmanager/ausmt/patches/sailfishos-patch-lockscreen-all-notifications ]; then
/usr/sbin/patchmanager -u sailfishos-patch-lockscreen-all-notifications || true
fi

%preun
if [ -d /var/lib/patchmanager/ausmt/patches/sailfishos-patch-lockscreen-all-notifications ]; then
/usr/sbin/patchmanager -u sailfishos-patch-lockscreen-all-notifications || true
fi

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/sailfishos-patch-lockscreen-all-notifications
